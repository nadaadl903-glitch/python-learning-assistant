from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

app = FastAPI(title="Python Learning Assistant")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = Ollama(
    model="llama3.2"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Python Learning Assistant API is running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    results = vectorstore.similarity_search(
        request.question,
        k=3
    )

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = f"""
You are a Python Learning Assistant.

Answer the question using ONLY the provided context.

If the answer is not available in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{request.question}

Answer:
"""

    answer = llm.invoke(prompt)

    sources = list(
        set(
            document.metadata.get("source", "Unknown")
            for document in results
        )
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }