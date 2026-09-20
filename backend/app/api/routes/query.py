from fastapi import APIRouter, Request

from app.schemas.query import (
    QuestionRequest,
    QueryResponse
)
from app.services.retrieval import retrieve_documents
from app.services.generation import generate_answer


router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query(request: QuestionRequest, app_request: Request):

    vectorstore = app_request.app.state.vectorstore
    llm = app_request.app.state.llm

    documents = retrieve_documents(
        vectorstore,
        request.question,
        k=3
    )

    answer = generate_answer(
        llm,
        request.question,
        documents
    )

    sources = list(dict.fromkeys(
        document.metadata.get("source", "Unknown")
        for document in documents
    ))

    return {
        "answer": answer,
        "sources": sources
    }