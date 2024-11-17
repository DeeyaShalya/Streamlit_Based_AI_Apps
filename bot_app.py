import streamlit as st
import google.generativeai as genai

genai.configure(api_key="Your_API_Key")

llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

st.title("Welcome to the Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "text": "Hi there! I am a helpful AI Assistant. How can I help you today?"}
    ]

for message in st.session_state.messages:
    if message["role"] == "ai":
        st.chat_message("ai").write(message["text"])
    else:
        st.chat_message("human").write(message["text"])

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    st.session_state.messages.append({"role": "human", "text": human_prompt})
    st.chat_message("human").write(human_prompt)

    response = chatbot.send_message(human_prompt)
    st.session_state.messages.append({"role": "ai", "text": response.text})
    st.chat_message("ai").write(response.text)
