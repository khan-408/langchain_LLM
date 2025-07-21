from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os



load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
model = ChatGroq(
    api_key=api_key,
    model ='llama3-8b-8192'
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a joke about {topic}.",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke in simple terms - {text}.',
    input_variables=['text']
)

gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2,model,parser)

})
chain = gen_chain | parallel_chain
result = chain.invoke({'topic':"Football"})

print(result)