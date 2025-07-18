from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()  # ✅ Make sure this is called first

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")


llm = ChatGroq(
    api_key=groq_api_key,
    model='llama3-8b-8192')

result = llm.invoke("What is the national game of india")

print(result.content)