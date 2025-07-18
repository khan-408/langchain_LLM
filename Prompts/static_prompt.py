from langchain_groq import ChatGroq
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

from dotenv import load_dotenv
load_dotenv()  # ✅ Make sure this is called first

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    api_key=groq_api_key,
    model='llama3-8b-8192'
)

st.header("Research paper Platform")
user_input = st.text_input("Enter your Prompt")

if st.button("Search"):
    result = model.invoke(user_input)
    st.write(result.content)