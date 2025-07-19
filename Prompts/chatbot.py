from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

groq_api = os.getenv('GROQ_API_KEY')

model = ChatGroq(
    api_key = groq_api,
    model = 'llama3-8b-8192'
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant.')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break
    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))

    print("AI: ", result.content)

print(chat_history)