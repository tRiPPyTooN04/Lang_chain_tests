from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import traceback

print("✅ Loading API Key...")
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
print("API Key Loaded:", "Yes" if api_key else "No")

try:
    print("🚀 Initializing Hugging Face model...")

    llm_endpoint = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-0528-Qwen3-8B",  # or another chat-compatible model
        task="text-generation",
        huggingfacehub_api_token=api_key,
        temperature=0.0,
        max_new_tokens=10,
    )

    model = ChatHuggingFace(llm=llm_endpoint)

    print("✉️ Sending test prompt...")
    response = model.invoke("What is the capital of India?")
    print("📬 Response:", response.content)

except Exception as e:
    print("❌ Error occurred:",str(e))
    traceback.print_exc()
