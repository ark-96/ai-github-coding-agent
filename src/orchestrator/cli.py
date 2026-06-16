import os
import sys
from pathlib import Path
from urllib import response

from dotenv import load_dotenv
from openai import OpenAI

target_file = Path("../ai-agent-portfolio/src/App.tsx")

user_request = "Add a testimonials section"

def read_file(file_path: Path) -> str:
    if not file_path.exists():
        print(f"ERROR: File {file_path} does not exist.")
        sys.exit(1)

    return file_path.read_text(encoding="utf-8")
    
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

def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY missing in .env")
        sys.exit(1)

    model = os.getenv("OPENAI_MODEL", "gpt-5.2")

    print("\n===  FILE PREVIEW ===\n")
    print(target_file.read_text(encoding="utf-8")[:500])  # Print the first 500 characters of the file

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input=build_prompt(target_file.read_text(encoding="utf-8"), user_request)
    )

    is_valid = validate_output(response.output_text)

    if not is_valid:
        print("ERROR: Model output failed validation.")
        sys.exit(1)

    write_file(target_file, response.output_text)

    print("\n=== VALIDATION ===\n")
    print(is_valid)

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)
    
    print("\n=== RESPONSE STATS ===\n")
    print("Input Length:", len(target_file.read_text(encoding="utf-8")))
    print("Output Length:", len(response.output_text))
    print("Tokens:", response.usage.total_tokens)
    print("Model:", response.model)


if __name__ == "__main__":
    main()