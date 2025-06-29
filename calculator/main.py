import os
from dotenv import load_dotenv
import sys

def main():
    pass

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)


if len(sys.argv) == 1:
    raise Exception("no prompt given")
    sys.exit(1)

user_prompt = sys.argv[1]

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

response_from_ai = client.models.generate_content(model = "gemini-2.0-flash-001", contents=messages,)

print(response_from_ai.text)

if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
    print("User prompt: " + user_prompt)
    print("Prompt tokens: " + str(response_from_ai.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response_from_ai.usage_metadata.candidates_token_count))
