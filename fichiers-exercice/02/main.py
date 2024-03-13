from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()

def format_response(result):
    print(Fore.GREEN + result.content + Fore.RESET)

def invoke(input):
    prompt = ChatPromptTemplate.from_template(
        "Tell me a short joke about {topic}"
    )
    model = ChatOpenAI(model="gpt-3.5-turbo")

    chain = prompt | model | format_response    

    return chain.invoke({"topic": input})


def start():
    print("MENU")
    print("====")
    print("[1]- Raconter une histoire drôle")
    print("[2]- Quitter")
    choice = input("Selection: ")
    if choice == "1":
        ask()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
        start()


def ask():
    """Poser une question à l'IA."""

    instructions = (
        "Taper'x' pour retourner au MENU MAIN.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)
    while True:

        user_input = input("Topic: ")
        # Exit
        if user_input == "x":
            start()
        else:
            # Generate a response
            invoke(user_input)
         


if __name__ == "__main__":
    start()

