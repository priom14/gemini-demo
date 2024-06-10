import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_reaponse(input,image):
    if input != " ":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini application")

input = st.text_input("Input: ", key = "input")

uploaded_file = st.file_uploader("Choose an image...",type=['jpg','jpeg','png', 'webp'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    

submit = st.button("Tell me about the image")


if submit:
    response = get_gemini_reaponse(input, image)
    st.subheader("Response")
    st.write(response)
