from App.story_prompt import generate_story
from App.image_generator import generate_image

def generate_character(name, genre, traits):
    result = generate_story(name, genre, traits)

    story, appearance = "", ""
    for line in result.split("\n"):
        if line.startswith("Story:"):
            story = line.replace("Story:", "").strip()
        elif line.startswith("Appearance:"):
            appearance = line.replace("Appearance:", "").strip()

    image_path = generate_image(appearance)
    return story, image_path
