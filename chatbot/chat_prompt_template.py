from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage

chat_template = ChatPromptTemplate([
    ('system','you are helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')

])

prompt = chat_template.invoke({'domain':'cricket','topic':'doosra'})

print(prompt)