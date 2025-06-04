
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    google_api_key=api_key,
    temperature=0,
    max_tokens=None,
    max_retries=6,
    stop=None
)



st.header("research tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt("template.json")

user_input = st.text_input("enter your prompt")



if st.button('Summarize'):

   chain = template | llm 
   result = chain.invoke({'paper_input': paper_input,
   'style_input': style_input,
   'length_input': length_input
   })
   st.write(result.content)

