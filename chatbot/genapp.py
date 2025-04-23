from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Langchain tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize the LLM (Language Model)
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",  # free-tier model
    google_api_key=gemini_api_key
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo With Google Generative AI')
input_text = st.text_input("Search the topic you want")

# Output parser and chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process user input
if input_text:
    st.write(chain.invoke({'question': input_text}))