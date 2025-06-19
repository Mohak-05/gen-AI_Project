# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'App')))

import streamlit as st
from generator import generate_character
from PIL import Image

st.set_page_config(page_title="🦙 LLaMA Character Generator", layout="centered")

st.title("🦙 LLaMA Character Generator")
st.markdown("Create unique characters with vivid stories and AI-generated portraits.")

with st.form("character_form"):
    name = st.text_input("Character Name")
    genre = st.selectbox("Genre", ["Fantasy", "Sci-Fi", "Historical", "Modern", "Cyberpunk", "Post-Apocalyptic", "Mystery", "Mythology"])
    traits = st.text_input("Character Traits (comma-separated)", placeholder="e.g., brave, cunning, sarcastic")

    submitted = st.form_submit_button("Generate Character")

if submitted:
    if not name or not traits:
        st.error("Please enter both a name and at least one trait.")
    else:
        with st.spinner("Generating your character..."):
            try:
                story, image_path = generate_character(name, genre, traits)
                st.subheader("📜 Character Story")
                st.write(story)

                st.subheader("🎨 Character Image")
                image = Image.open(image_path)
                st.image(image, caption=f"{name} - {genre}", use_column_width=True)

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
