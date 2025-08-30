from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question,image):
    if input!="":
        response = model.generate_content([question,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Pro Vision Chatbot", page_icon=":robot_face:")
st.header("Gemini Pro Vision Chatbot")

input = st.text_input("Ask a question:", "", key="input")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit  = st.button("Submit")

if submit:
    if image is not None:
        response = get_gemini_response(input, image)
        st.subheader("Response:")
        st.write(response)