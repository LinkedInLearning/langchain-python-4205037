import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
)
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Chroma
from colorama import Fore

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "gpt-3.5-turbo"

template: str = """/
Vous êtes un spécialiste du support client. Vous assistez les utilisateurs avec des demandes générales basées sur {context} et des problèmes techniques. /
Si vous ne connaissez pas la réponse, vous invitez l'utilisateur à joindre le service support au téléphone ou par mail 
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_message_prompt = HumanMessagePromptTemplate.from_template(
    input_variables=["question", "context"],
    template="{question}",
)
chat_prompt_template = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

model = ChatOpenAI()

def load_documents():
    """Load a file from path, split it into chunks, embed each chunk and load it into the vector store."""
    loader = TextLoader("./docs/faq_fr.txt")
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    
    documents = loader.load()
    chunks = text_splitter.split_documents(documents)
    print(f"You have {len(documents)} documents and {len(chunks)} chunks.")
    return chunks


def load_embeddings(documents, user_query):
    """Create a vector store from a set of documents."""
    db = Chroma.from_documents(documents, OpenAIEmbeddings())
    docs = db.similarity_search(user_query)
    # print(docs)
    return db.as_retriever()


def generate_response(retriever, query):
    """Generate a response to a user query."""
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | chat_prompt_template
        | model
        | StrOutputParser()
    )
    return chain.invoke(query)


def query(query):
    """Load documents, create a vector store, and generate a response to a user query."""
    documents = load_documents()
    retriever = load_embeddings(documents, query)
    response = generate_response(retriever, query)
    print(Fore.GREEN + response)


query("Quelles sont les horaires d'ouverture ?")
