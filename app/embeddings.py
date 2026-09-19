from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

test_text = "Python is a programming language."

vector = embeddings.embed_query(test_text)

print("Embedding created successfully!")
print("Vector length:", len(vector))