from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.query import router as query_router
from app.services.retrieval import create_vectorstore
from app.services.generation import create_llm


@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.vectorstore = create_vectorstore()
    app.state.llm = create_llm()

    yield


app = FastAPI(
    title="Python Learning Assistant",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    query_router
)