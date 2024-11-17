import streamlit as st
import google.generativeai as genai

genai.configure(api_key="Your_API_Key")
llm = genai.GenerativeModel("models/gemini-1.5-flash")
code_review_bot = llm.start_chat(history=[])

st.set_page_config(
    page_title="Code Review Assistant",
    page_icon="🤖",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
        margin-top: -50px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
    }
    .sidebar-content {
        font-size: 1rem;
        color: #333333;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #aaaaaa;
        margin-top: 50px;
    }
    </style>
    <div>
        <p class="main-title">Code Review Assistant 🤖</p>
        <p class="sub-title">Your AI-powered companion for reviewing code and suggesting fixes.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Welcome! :wave:")
    st.markdown(
        """
        This application helps you:
        - Identify potential bugs in your code.
        - Receive optimized, corrected code snippets.
        - Enhance your programming with AI assistance!
        """
    )
    st.markdown(
        "#### 💻 Supported Languages: \n- Python \n- Java \n- C \n- C++"
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Code-icon.svg/120px-Code-icon.svg.png",
        width=200,
    )

st.markdown("---")
language = st.selectbox(
    "🌐 Select Programming Language:",
    ["Python", "Java", "C", "C++"],
    help="Choose the language of your code for review."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "ai",
            "text": (
                "Welcome! I can help review your code for bugs and provide fixes. "
                "Select your language and paste your code below to get started."
            ),
        }
    ]

for message in st.session_state.messages:
    if message["role"] == "ai":
        st.chat_message("ai").write(message["text"])
    else:
        st.chat_message("human").write(message["text"])

st.markdown(
    f"""
    ### ✏️ Paste Your {language} Code Below:
    """
)
code = st.text_area(f"{language} Code:", height=200, placeholder="Write or paste your code here...")

if st.button("🚀 Submit Code for Review"):
    if code.strip() == "":
        st.error("❌ Please paste your code before submitting.")
    else:
        st.session_state.messages.append({"role": "human", "text": code})
        st.chat_message("human").write(code)

        with st.spinner("🧠 Analyzing your code..."):
            try:
                prompt = f"Review the following {language} code, identify potential bugs, and suggest fixes:\n\n{code}"
                response = code_review_bot.send_message(prompt)

                st.session_state.messages.append({"role": "ai", "text": response.text})
                st.chat_message("ai").write(response.text)
            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")

st.markdown(
    """
    <div class="footer">
        <hr>
        <p>Developed using Streamlit and Generative AI</p>
    </div>
    """,
    unsafe_allow_html=True,
)
