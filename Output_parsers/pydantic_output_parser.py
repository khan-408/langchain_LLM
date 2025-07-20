from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
model = ChatGroq(
    api_key=api_key,
    model ='llama3-8b-8192'
)


class Person(BaseModel):
    name:str=Field(description='Name of the person.')
    age:int=Field(gt=18, description='Age of the Person.')
    city:str=Field(description='Name of the city where the person belongs to.')


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser 

final_result = chain.invoke({'place':'sri lanka'})

print(final_result)