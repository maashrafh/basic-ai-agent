import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from available_functions import available_functions, call_function
from config import system_prompt


def main():
    if len(sys.argv) <= 1:
        print(f'no prompt was provided.')
        sys.exit(1)

    global verbose
    verbose = "--verbose" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    agent_loop(client)


def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
    )
    return response


def agent_loop(client):
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]

    loop = True
    while (loop == True):
        try:
            response = generate_content(client, messages)
        except Exception as e:
            print(f'Exeception occurred during content generation: {e}')
            break

        loop = process_response(messages, response)

def process_response(messages, response):
    loop = True
    if len(messages) > 20:
        loop = False
        return loop

    if response.function_calls:
        func_response = process_func_call(response)
        messages.append(func_response)
    elif response.text:
        process_text_response(response)
        loop = False
    else:
        raise Exception(f"Unknown response received.")
    return loop

def process_text_response(response):
    response_text = response.candidates[0].content.parts[0].text
    print(response_text)
    if verbose:
        print(f'User prompt: {sys.argv[1]}')
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(
            f'Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}')

def process_func_call(response):
    for func_call in response.function_calls:
        result = call_function(func_call, verbose)
        func_response = result.parts[0].function_response.response

        if func_response == None:
            raise Exception(f"No results from function call.")

        if verbose:
            print(f"-> {func_response}")

        return types.Content(role="user", parts=[types.Part(text=func_response["result"])])

if __name__ == "__main__":
    main()
