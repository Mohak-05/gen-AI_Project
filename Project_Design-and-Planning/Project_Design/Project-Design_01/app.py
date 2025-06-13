# app.py
import streamlit as st
from prompt_template import build_prompt

st.set_page_config(page_title="Character Generator", layout="centered")
st.title("🧠 AI-Powered Character Description Generator")

# User Inputs
name = st.text_input("Character Name")
role = st.text_input("Character Role (e.g., Hero, Villain)")
traits = st.text_area("Character Traits (comma-separated)")
setting = st.text_input("Story Setting (e.g., Sci-fi, Medieval)")
age = st.number_input("Age", min_value=0, max_value=150, step=1)
details = st.text_area("Other Specific Details")

if st.button("Generate Description"):
    prompt = build_prompt(name, role, traits, setting, age, details)
    # Placeholder output for now
    st.markdown("### 📝 Character Description:")
    st.success(f"(Generated based on prompt):\n\n{prompt}")
