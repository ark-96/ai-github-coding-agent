import os
import sys
from pathlib import Paths

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY missing in .env")
        sys.exit(1)

    model = os.getenv("OPENAI_MODEL", "gpt-5.2")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=model,
        input="Reply with exactly: orchestration environment ready"
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(response.output_text)


if __name__ == "__main__":
    main()