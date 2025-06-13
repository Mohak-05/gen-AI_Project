import streamlit as st
from App.generator import generate_character

st.set_page_config(page_title="AI Character Generator", layout="wide")

st.title("🧙 AI-Powered Character Generator")

with st.form("char_form"):
    name = st.text_input("Character Name", "Aeris")
    genre = st.selectbox("Genre", ["Fantasy", "Sci-Fi", "Steampunk"])
    traits = st.text_area("Character Traits", "Brave, exiled princess, secretly half-dragon")
    submitted = st.form_submit_button("Generate")

if submitted:
    with st.spinner("Generating story and image..."):
        story, image_path = generate_character(name, genre, traits)

    st.subheader("📝 Story")
    st.write(story)

    st.subheader("🎨 Portrait")
    st.image(image_path, use_column_width=True)
