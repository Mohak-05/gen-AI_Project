# generator.py

from story_prompt import generate_story
from image_generator import generate_image

def generate_character(name, genre, traits):
    print("🧠 Generating character story...")
    story = generate_story(name, genre, traits)

    print("🎨 Generating character image...")
    image_prompt = f"{name}, a {genre} character with traits: {traits}"
    image_path = generate_image(image_prompt)

    return story, image_path
