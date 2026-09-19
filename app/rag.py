from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Load vector database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# LLM
llm = Ollama(
    model="llama3.2"
)

# User question
question = "What is a Python function?"

# Retrieve relevant chunks
results = vectorstore.similarity_search(question, k=3)

# Combine retrieved context
context = "\n\n".join(
    document.page_content for document in results
)

# Prompt
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

# Generate answer
answer = llm.invoke(prompt)

print("\nAnswer:")
print(answer)

print("\nSources:")
for document in results:
    print("-", document.metadata.get("source", "Unknown"))