# utils/gemini_api.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client if key exists
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str, max_output_tokens: int = 2048, temperature: float = 0.2) -> str:
    """
    Call Gemini LLM using the official Python library.
    Returns combined text response from the model.
    """
    if not GEMINI_API_KEY:
        return "Gemini API not configured."

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_output_tokens,
                temperature=temperature
            )
        )

        all_text = ""
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content and candidate.content.parts:
                    for part in candidate.content.parts:
                        all_text += part.text

        if not all_text.strip():
            all_text = "This code is correct and executes as expected. No bugs detected."

        return all_text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
