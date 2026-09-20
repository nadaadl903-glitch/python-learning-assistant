from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

from app.core.config import (
    VECTOR_STORE_PATH,
    EMBEDDING_MODEL
)


def create_vectorstore():
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    return Chroma(
        persist_directory=VECTOR_STORE_PATH,
        embedding_function=embeddings
    )


def retrieve_documents(vectorstore, question: str, k: int = 3):
    return vectorstore.similarity_search(
        question,
        k=k
    )