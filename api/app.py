from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Create FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"  # fixed typo from 'decsription'
)

# ✅ Root route to fix 404 on /
@app.get("/")
def read_root():
    return {"message": "Welcome to the Langchain Server! Visit /docs to explore the API."}

# OpenAI route
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Ollama route - Poem generator
llm = Ollama(model="llama3")
prompt1 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years old child with 100 words")
add_routes(
    app,
    prompt1 | llm,
    path="/poem"
)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)