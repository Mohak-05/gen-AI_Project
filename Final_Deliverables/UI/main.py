# # main.py
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'App')))

# import streamlit as st
# from generator import generate_character
# from PIL import Image

# st.set_page_config(page_title="🦙 LLaMA Character Generator", layout="centered")

# st.title("🦙 LLaMA Character Generator")
# st.markdown("Create unique characters with vivid stories and AI-generated portraits.")

# with st.form("character_form"):
#     name = st.text_input("Character Name")
#     genre = st.selectbox("Genre", ["Fantasy", "Sci-Fi", "Historical", "Modern", "Cyberpunk", "Post-Apocalyptic", "Mystery", "Mythology"])
#     traits = st.text_input("Character Traits (comma-separated)", placeholder="e.g., brave, cunning, sarcastic")

#     submitted = st.form_submit_button("Generate Character")

# if submitted:
#     if not name or not traits:
#         st.error("Please enter both a name and at least one trait.")
#     else:
#         with st.spinner("Generating your character..."):
#             try:
#                 story, image_path = generate_character(name, genre, traits)
#                 st.subheader("📜 Character Story")
#                 st.write(story)

#                 st.subheader("🎨 Character Image")
#                 image = Image.open(image_path)
#                 st.image(image, caption=f"{name} - {genre}", use_column_width=True)

#             except Exception as e:
#                 st.error(f"❌ An error occurred: {e}")
# main.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'App')))

import streamlit as st
from generator import generate_character
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="🦙 LLaMA Character Generator", layout="centered", initial_sidebar_state="collapsed")

# --- Hyper-Modern CSS Styling ---
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
    /* Animated gradient background */
    @keyframes gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .stApp {
      background: linear-gradient(-45deg, #ff4b1f, #1fddff, #ff1f8b, #1fff61);
      background-size: 400% 400%;
      animation: gradient 20s ease infinite;
      font-family: 'Roboto', sans-serif;
    }
    /* Title styling */
    .title {
      font-family: 'Roboto', sans-serif;
      font-size: 3rem;
      color: #ffffff;
      text-align: center;
      animation: fadeInDown 1.5s ease-out;
      margin-top: 1rem;
    }
    @keyframes fadeInDown {
      0% { opacity: 0; transform: translateY(-50px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    /* Form input styling overrides */
    .stTextInput > div > div > input {
      border-radius: 0.5rem;
      padding: 0.5rem;
    }
    .stSelectbox > div > div > div {
      border-radius: 0.5rem;
      padding: 0.5rem;
    }
    /* Spinner alignment */
    .stSpinner div {
      text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown("<h1 class='title'>🦙 LLaMA Character Generator</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='color:#ffffff; text-align:center;'>Create unique characters with vivid stories and AI-generated portraits.</h4>",
    unsafe_allow_html=True
)

# --- Character Form ---
with st.form("character_form"):
    name = st.text_input("Character Name")
    genre = st.selectbox(
        "Genre",
        ["Fantasy", "Sci-Fi", "Historical", "Modern", "Cyberpunk", "Post-Apocalyptic", "Mystery", "Mythology"]
    )
    traits = st.text_input(
        "Character Traits (comma-separated)",
        placeholder="e.g., brave, cunning, sarcastic"
    )

    submitted = st.form_submit_button("Generate Character")

# --- Display Results ---
if submitted:
    if not name or not traits:
        st.error("Please enter both a name and at least one trait.")
    else:
        with st.spinner("Generating your character..."):
            try:
                story, image_path = generate_character(name, genre, traits)

                st.markdown("<h3 style='color:#ffffff; text-align:center;'>📜 Character Story</h3>", unsafe_allow_html=True)
                st.write(story)

                st.markdown("<h3 style='color:#ffffff; text-align:center;'>🎨 Character Image</h3>", unsafe_allow_html=True)
                image = Image.open(image_path)
                st.image(image, caption=f"{name} - {genre}", use_container_width=True)

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
