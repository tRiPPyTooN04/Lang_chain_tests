from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'E:/huggingface_cache'

try:
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs=dict(
            temperature=0.5,
            max_new_tokens=10
        )
    )

    model = ChatHuggingFace(llm)
    result = model.invoke("What is the capital of India?")
    print(result.content)

except Exception as e:
    print(f"An error occurred: {e}")