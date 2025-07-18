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

paper_input = st.selectbox("Select search paper name", ["Attention is all your need", "BERT:Pre training of deep bidirectional Transformers", "GPT-3: Language Models are Few Shot Learners", "Diffusion Models veat GANs on Image Synthesis"])


style_input = st.selectbox("Select Explanation Style",["Beginner Friendly","Technical"," Code-Oriented","Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short", "Moderate", "Lenghty"])


template = load_prompt('template.json')


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({'paper_input':paper_input,
                        'style_input':style_input,
                        'length_input': length_input
                        })
    
    st.write(result.content)