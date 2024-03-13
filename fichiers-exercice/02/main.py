from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()

def format_response(result):
    print(Fore.GREEN + result.content + Fore.RESET)

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
model = ChatOpenAI(model="gpt-3.5-turbo")

chain = prompt | model | format_response    

chain.invoke({"topic": "chickens"})
