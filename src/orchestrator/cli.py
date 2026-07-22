import os
import shutil
import sys
from pathlib import Path
import subprocess
from urllib import response

from dotenv import load_dotenv
from openai import OpenAI

target_file = Path("../ai-agent-portfolio/src/App.tsx")

def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY missing in .env")
        sys.exit(1)

    return api_key

def read_file(file_path: Path) -> str:
    if not file_path.exists():
        print(f"ERROR: File {file_path} does not exist.")
        sys.exit(1)

    return file_path.read_text(encoding="utf-8")

def get_user_request() -> str:
    if len(sys.argv) < 2:
        print("ERROR: User request not provided. Usage: python src.orchestratorcli 'Your request here'")
        sys.exit(1)

    return sys.argv[1]

def build_prompt(file_content: str, user_request: str) -> str:
    return f"""
You are acting as a software engineer. 
You will be provided with the content of a file and a user request. 
Your task is to modify the file content according to the user request.      

File Content:
{file_content}

User Request:
{user_request}

Return a modified version of the file content that fulfills the user request.
Do not include any explanations or additional text, only return the modified file content.
"""

def generate_updated_file(client: OpenAI, model: str, prompt: str) -> str:
    response = client.responses.create(
        model=model,
        input=prompt,
    )

    print("\n=== RESPONSE STATS ===\n")
    print("Output Length:", len(response.output_text))
    print("Tokens:", response.usage.total_tokens)
    print("Model:", response.model)

    return response.output_text

def validate_output(updated_code: str) -> bool:
    # Basic validation: Check if the output is not empty and contains some code structure
    if not updated_code.strip():
        print("ERROR: Output is empty.")
        return False

    if "```" in updated_code:
        print("ERROR: Output contains markdown code blocks.")
        return False

    if len(updated_code) < 100:
        print("ERROR: Output is too short.")
        return False

    return True

def write_file(file_path: Path, content: str) -> None:
    file_path.write_text(content, encoding="utf-8")

def run_build_validation(file_path: Path) -> bool:
    try:
        # Determine the project directory to run `npm run build` in.
        # If `file_path` is a file, walk up to find the nearest package.json.
        project_dir = Path(file_path)
        if project_dir.is_file():
            project_dir = project_dir.parent

        # Walk up until we find a package.json (max 5 levels), otherwise use the immediate parent.
        found = False
        for _ in range(6):
            if (project_dir / "package.json").exists():
                found = True
                break
            if project_dir.parent == project_dir:
                break
            project_dir = project_dir.parent

        if not found:
            print("ERROR: Could not find package.json for the target project.")
            return False

        result = subprocess.run(
            "npm run build",
            cwd=str(project_dir),
            check=True,
            capture_output=True,
            text=True,
            shell=True,
        )
        print("\n=== BUILD OUTPUT ===\n")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("\n=== BUILD ERROR ===\n")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        print(f"BUILD VALIDATION FAILED — exit code {e.returncode}")
        return False
    except FileNotFoundError:
        print("ERROR: 'npm' executable not found. Is Node.js installed and on PATH?")
        return False
    except NotADirectoryError as e:
        print(f"ERROR: Invalid directory for build: {e}")
        return False

def main() -> None:
    load_dotenv()

    api_key = get_api_key()
    model = os.getenv("OPENAI_MODEL", "gpt-5.2")
    current_code = read_file(target_file)

    print("\n===  FILE PREVIEW ===\n")
    print(current_code[:500])  # Print the first 500 characters of the file

    client = OpenAI(api_key=api_key)
    user_request = get_user_request()
    prompt = build_prompt(current_code, user_request)   

    response = generate_updated_file(client=client, model=model, prompt=prompt)

    is_valid = validate_output(updated_code=response)

    print("\n=== VALIDATION ===\n")
    print(is_valid)

    if not is_valid:
        print("ERROR: Model output failed validation.")
        sys.exit(1)

    write_file(target_file, response)

    print("\n=== FILE UPDATED ===\n")
    print(f"Updated: {target_file}")

    build_passed = run_build_validation(target_file)

    if not build_passed:
        sys.exit(1)


if __name__ == "__main__":
    main()