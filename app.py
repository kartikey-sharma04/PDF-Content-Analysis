import streamlit as st
import json
from utils.question_generator import generate_question, extract_json

def load_pdf_data(json_file="output.json"):
    with open(json_file, "r") as f:
        return json.load(f)

st.set_page_config(page_title="AI PDF Question Generator", layout="wide")

st.title("AI-Powered PDF Question Generator")
st.markdown("Generate MCQs from educational PDF content using Groq/Mixtral.")

pdf_data = load_pdf_data()
pages = [f"Page {entry['page']}" for entry in pdf_data]
choice = st.selectbox("Select a page", pages)

selected_page = int(choice.split()[1]) - 1
page_data = pdf_data[selected_page]

st.subheader("Extracted Text")
st.text_area("Text", value=page_data['text'], height=250)

if page_data['images']:
    st.subheader("Extracted Images")
    for img in page_data['images']:
        st.image(img, use_column_width=True)

from utils.question_generator import generate_question, extract_json

if st.button("✨ Generate Question"):
    with st.spinner("Thinking..."):
        raw_output = generate_question(page_data['text'])
        parsed = extract_json(raw_output)

        if "error" in parsed:
            st.error(parsed["error"])
        else:
            st.success("✅ Question Generated!")
            st.json(parsed)

