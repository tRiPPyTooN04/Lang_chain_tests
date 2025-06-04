from langchain_core.messages  import SystemMessage,HumanMessage,AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  
        google_api_key=api_key,
        temperature=0  ,
        max_tokens= 50,
        max_retries=6,
        stop=None
    )
messages = [
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content ='tell me about langchain' )
]
result = llm.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)