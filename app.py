from dotenv import load_dotenv

load_dotenv()  # access .env

import streamlit as st
import os

import google.generativeai as genai

def configure_genai():
    os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load OpenAI model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

#initialize Streamlit app
st.set_page_config(page_title="Chatbot")

# main content layout
st.title("Gemini Chatbot")

#collecting input
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# if ask button is clicked
if submit_button:
    configure_genai()
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
    
    # add a button to simulate redirection
    if st.button("Go to Another Page"):
        #for demonstration, let's update the message
        st.write("Redirection Successful!")
