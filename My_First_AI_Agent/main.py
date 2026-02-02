import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.')
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata found in the response.")
    Prompt_Tokens = response.usage_metadata.prompt_token_count
    Response_Tokens = response.usage_metadata.candidates_token_count    
    print(f"Prompt tokens: {Prompt_Tokens}")
    print(f"Response tokens: {Response_Tokens}")
    print(response.text)


if __name__ == "__main__":
    main()
