from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_STORE_PATH = os.getenv(
    "VECTOR_STORE_PATH",
    str(BASE_DIR / "data" / "vector_store")
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama3.2"
)