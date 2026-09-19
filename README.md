# 🐍 Python Learning Assistant

A Retrieval-Augmented Generation (RAG) assistant that answers questions about Python programming using a collection of educational documents.

## Project Overview

The Python Learning Assistant uses RAG to retrieve relevant information from the provided Python documents and generate answers using a local Large Language Model (LLM).

The system answers questions based only on the retrieved document context and provides the sources used to generate each answer.

## Architecture

Documents → Loading → Chunking → Embeddings → Chroma Vector Database → Retrieval → Prompt + Context → Ollama LLM → Answer + Sources → FastAPI → Streamlit

## Technologies Used

- Python
- LangChain
- ChromaDB
- Ollama
- Llama 3.2
- Nomic Embed Text
- FastAPI
- Streamlit

## Project Structure

rag assi/
├── app/
│   ├── load_documents.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   └── rag.py
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── data/
│   ├── python_basics.txt
│   ├── variabls_data_types.txt
│   ├── functions.txt
│   ├── oop.txt
│   ├── exceptions.txt
│   └── file_handling.txt
├── evaluation.txt
├── requirements.txt
└── README.md

## How It Works

1. Python documents are loaded from the data folder.
2. Documents are split into smaller chunks.
3. Each chunk is converted into an embedding using nomic-embed-text.
4. Embeddings are stored in ChromaDB.
5. When the user asks a question, relevant chunks are retrieved.
6. The retrieved context is sent to the local llama3.2 model through Ollama.
7. The model generates an answer based only on the provided context.
8. The system returns the answer and its sources.
9. FastAPI provides the backend API.
10. Streamlit provides the user interface.

## Running the Project

### 1. Activate the virtual environment

`bash
venv\Scripts\activate
2. Start the FastAPI backend
uvicorn backend.main:app --reload
3. Start the Streamlit frontend
Open another terminal and run:
streamlit run frontend/app.py
Then open the Streamlit URL shown in the terminal.
Evaluation
The system was tested using 10 evaluation questions covering the provided Python learning materials.
Additional questions outside the provided documents were used to verify that the assistant does not generate unsupported answers.
Key Features
Local LLM using Ollama
Retrieval-Augmented Generation
Semantic document retrieval
Source attribution
FastAPI backend
Streamlit frontend
Evaluation questions
No external LLM API required