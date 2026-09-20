import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("API key could not be found. Check the .env file for the correct key.")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

parser = argparse.ArgumentParser(description= "Herms")
parser.add_argument("user_prompt", type=str, help="Prompt to send to the model")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
print(args.verbose)

messages = [
    {"role": "user", "content": args.user_prompt},
]
response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

print(response.choices[0].message.content)
if response.usage is None:
    raise RuntimeError("Response usage is None. This may indicate an issue with the API response.")
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")


def main():
    print("Answer brought to you by Herms!")


if __name__ == "__main__":
    main()
