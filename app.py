import streamlit as st
from add_llm import chatBot
import time

st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .stTextInput input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .chatbox {
        background-color: #fff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 ChatBot for Deep Learning")

chat_container = st.container()

# Take user input
Q = st.text_input("💬 Enter Your Question", key="user_input")

if st.button("🚀 Ask Chatbot"):
    if Q.strip(): 
        with chat_container:
            with st.spinner("Thinking... 🤔"):
                time.sleep(1.5)  
                res = chatBot(Q)

            st.markdown(f"""
                <div class="chatbox">
                    <b>🧠 Chatbot:</b><br> {res['result']}
                </div>
            """, unsafe_allow_html=True)
