from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()  # ✅ Make sure this is called first

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    api_key=groq_api_key,
    model='llama3-8b-8192'
)

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")

]

result = model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)