import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

target_file = Path("../ai-agent-portfolio/src/App.tsx")

user_request = "Add a testimonials section"

def read_file(file_path: Path) -> str:
    if not file_path.exists():
        print(f"ERROR: File {file_path} does not exist.")
        sys.exit(1)

    with open(file_path, "r") as f:
        return f.read()
    
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

def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY missing in .env")
        sys.exit(1)

    model = os.getenv("OPENAI_MODEL", "gpt-5.2")

    print("\n===  FILE PREVIEW ===\n")
    print(read_file(target_file)[:500])  # Print the first 500 characters of the file

    client = OpenAI(api_key=api_key)

    # response = client.responses.create(
    #     model=model,
    #     input=build_prompt(read_file(target_file), user_request)
    # )

    response = client.responses.create(
        model=model,
        input="Reply with exactly: orchestration environment ready"
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)

    
    print("\n=== RESPONSE STATS ===\n")
    print("Input Length:", len(read_file(target_file)))
    print("Output Length:", len(response.output_text))

    print("Tokens:", response.usage.total_tokens)
    # print("Cost (USD):", response.usage.total_cost)
    print("Time (ms):", response.usage)
    print("Model:", response.model)


if __name__ == "__main__":
    main()