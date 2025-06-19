# image_generator.py

from google import genai
from google.genai import types
from config import GEMINI_IMAGE_KEY, GEMINI_IMAGE_MODEL
from PIL import Image
from io import BytesIO

# Configure the Gemini client with your API key
# Make sure GEMINI_IMAGE_KEY is set in your config.py
client = genai.Client(api_key=GEMINI_IMAGE_KEY)

def generate_image(prompt):
    """
    Calls Google Gemini's image generation API using the provided prompt.
    Saves the resulting image as 'generated_image.png' and returns its file path.
    """
    # Request only the IMAGE modality
    response = client.models.generate_content(
        model=GEMINI_IMAGE_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]
        )
    )

    # Extract image from the response
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            img = Image.open(BytesIO(part.inline_data.data))
            out_path = "generated_image.png"
            img.save(out_path)
            return out_path

    # If no image data was returned, raise an error
    raise RuntimeError("No image returned from Gemini API")
