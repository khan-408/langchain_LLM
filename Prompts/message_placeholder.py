from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder

chat_template = ChatMessagePromptTemplate([
    ('system', 'You are a helpful customer support system.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)