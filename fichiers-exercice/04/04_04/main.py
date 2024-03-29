#!/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import openai
import os

load_dotenv()
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

# créer un serveur API avec FastAPI
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# ajouter des routes pour les modèles de chat
# lancer 'pip install pydantic==1.10.13' pour accéder /docs
add_routes(
    app,
    model,
    path="/chat",
)

add_routes(
    app,
    prompt | model,
    path="/generate",
)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()