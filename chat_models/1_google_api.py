from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

print("✅ Loading API Key...")
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("API Key Loaded:", "Yes" if api_key else "No")

try:
    print("🚀 Initializing Gemini model...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  
        google_api_key=api_key,
        temperature=0  ,
        max_tokens= 50,
        max_retries=6,
        stop=None
    )

    print("✉️ Sending test prompt...")
    response = llm.invoke("What is the capital of India?")
    print("📬 Response:", response.content )

except Exception as e:
    print("❌ Error occurred:", e)
