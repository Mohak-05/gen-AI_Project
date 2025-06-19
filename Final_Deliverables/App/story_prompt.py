# story_prompt.py

import requests
from config import LLAMA_API_URL, LLAMA_API_KEY, TIMEOUT

def generate_story(name, genre, traits):
    prompt = (
        f"Create a vivid, detailed backstory and description for a fictional character.\n"
        f"Name: {name}\n"
        f"Genre: {genre}\n"
        f"Traits: {traits}\n" 
        f"Write it in an immersive, engaging style with rich language."
    )

    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json" 
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a masterful storyteller AI."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.85,
        "max_tokens": 800
    }

    response = requests.post(LLAMA_API_URL, headers=headers, json=payload, timeout=TIMEOUT)

    if response.status_code != 200:
        raise RuntimeError(f"Story generation failed: {response.text}")

    return response.json()["choices"][0]["message"]["content"]
