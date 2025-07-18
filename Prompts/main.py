#Try it with FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# LangChain Groq model
model = ChatGroq(
    api_key=groq_api_key,
    model="llama3-8b-8192"
)

# Load prompt template
template = load_prompt("template.json")

# Combine prompt with model
chain = template | model

# FastAPI app
app = FastAPI()

# Request body schema
class SummaryRequest(BaseModel):
    paper_input: str
    style_input: str
    length_input: str

@app.post("/summarize/")
def summarize(req: SummaryRequest):
    result = chain.invoke({
        "paper_input": req.paper_input,
        "style_input": req.style_input,
        "length_input": req.length_input
    })
    return {"summary": result.content}
