import streamlit as st
from langchain.schema import HumanMessage
from utils.chat_handler import get_chatbot_response
from utils.log_handler import log_chat, clear_logs
from config import OPENAI_API_KEY

# Streamlit UI Configuration
st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 LangChain Chatbot with OpenAI API")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["gpt-3.5-turbo", "gpt-4"])
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        clear_logs()
        st.success("Chat history cleared!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input
user_input = st.text_input("Ask something:")

if user_input and OPENAI_API_KEY:
    # Append user's message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Get AI response using chat_handler.py
    response = get_chatbot_response(st.session_state.messages, model=model_name)
    
    # Store AI response in history
    st.session_state.messages.append(response)

    # Log the conversation
    log_chat(user_input, response.content)

# Display chat history (Fix: Unique keys for `st.text_area()` to prevent duplicate IDs)
for i, msg in enumerate(st.session_state.messages):
    role = "You:" if isinstance(msg, HumanMessage) else "🤖 AI:"
    st.text_area(role, value=msg.content, height=100, disabled=True, key=f"msg_{i}")
