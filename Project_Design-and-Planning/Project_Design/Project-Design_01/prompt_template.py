# prompt_template.py

def build_prompt(name, role, traits, setting, age, details):
    prompt = f"""
Create a detailed and engaging character description for the following character:

Name: {name}
Role: {role}
Age: {age}
Setting: {setting}
Traits: {traits}
Details: {details}

Make the description vivid, creative, and suitable for storytelling.
"""
    return prompt.strip()
