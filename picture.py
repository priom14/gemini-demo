import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_reaponse(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")
st.header("LLM application")

input = st.text_input("Input: ", key = "input")
submit = st.button("Ask your question")

if submit:
    response = get_gemini_reaponse(input)
    st.subheader("The response is")
    st.write(response)