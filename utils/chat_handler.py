#from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

from langchain.schema import AIMessage, HumanMessage
from config import OPENAI_API_KEY

def get_chatbot_response(messages, model="gpt-3.5-turbo"):
    """Sends chat history to OpenAI API and gets AI response."""
    try:
        llm = ChatOpenAI(model_name=model, openai_api_key=OPENAI_API_KEY)
        return llm.invoke(messages)

    except Exception as e:
        return AIMessage(content=f"Error: {str(e)}")
