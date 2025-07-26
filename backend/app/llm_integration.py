import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_response(prompt: str):
    url = "https://api.groq.com/llm"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {"prompt": prompt, "max_tokens": 150}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("text", "I'm not sure.")
    return "Error: Unable to fetch AI response."
