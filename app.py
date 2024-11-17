import streamlit as st

import google.generativeai as genai

genai.configure(api_key="Your_API_Key")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.title("Data Science Tutor Application")

user_prompt = st.text_input("Enter your query:",
              placeholder="Type your query here...")

btn_click = st.button("Generate Response")

if btn_click==True:
    #generate responce, configure, call gemini or gpt model
    response = model.generate_content(user_prompt)
    st.write(response.text)
