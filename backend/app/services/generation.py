from langchain_community.llms import Ollama

from app.core.config import LLM_MODEL


def create_llm():
    return Ollama(
        model=LLM_MODEL
    )


def generate_answer(llm, question: str, documents):
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a Python Learning Assistant.

Answer the question using ONLY the provided context.

If the answer is not available in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt)