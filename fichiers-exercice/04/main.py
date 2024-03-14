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


# ajouter des routes pour les modèles de chat



if __name__ == "__main__":
    pass