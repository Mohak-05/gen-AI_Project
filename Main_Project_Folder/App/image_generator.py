from diffusers import StableDiffusionPipeline
import torch

# Load once
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt):
    image = pipe(prompt).images[0]
    path = f"Outputs/character_{hash(prompt)}.png"
    image.save(path)
    return path
