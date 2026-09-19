from load_documents import documents
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

# 2. Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# 3. Store chunks in Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

# 4. Test retrieval
query = "What is a Python function?"
results = vectorstore.similarity_search(query, k=3)

print("\nRetrieved chunks:\n")

for i, result in enumerate(results):
    print(f"--- Result {i + 1} ---")
    print(result.page_content[:500])