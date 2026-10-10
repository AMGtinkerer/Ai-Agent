import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions
import json
from functions.get_files_info import schema_get_files_info






def main():



    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("API key could not be found. Check the .env file for the correct key.")

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    parser = argparse.ArgumentParser(description= "Herms")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the model")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    

    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
    ]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )
    message = response.choices[0].message

    if message.tool_calls is not None:

        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(message.content)

    
    if response.usage is None:
        raise RuntimeError("Response usage is None. This may indicate an issue with the API response.")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print("Answer brought to you by Herms!")


if __name__ == "__main__":
    main()
