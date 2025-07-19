from langchain_core.prompts import ChatPromptTemplate

chat_temlate = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain is simple terms, What is {topic}.')

])


prompt = chat_temlate.invoke({'domain':'cricket','topic':'dusra'})
print(prompt)