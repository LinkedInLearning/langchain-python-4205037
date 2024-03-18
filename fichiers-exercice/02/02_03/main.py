from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", api_key)
response = model.invoke("Tell me a short joke about horses")
print(response) 