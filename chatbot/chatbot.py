from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv
import os
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

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
chat_history = [
    SystemMessage(content="you are a helpful ai assistant")
]
while True:
    user_input =  input('you: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit': 
       break 
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)


print(chat_history)
