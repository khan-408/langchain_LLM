from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate,load_prompt

from dotenv import load_dotenv
load_dotenv()  # ✅ Make sure this is called first

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    api_key=groq_api_key,
    model='llama3-8b-8192'
)

template = PromptTemplate(
    template = "Greet this person in 5 language. The name of the person is {name}",
    input_variables={'name'}
)

prompt = template.invoke({'name':'Zaid'})

result = model.invoke(prompt)

print(result.content)