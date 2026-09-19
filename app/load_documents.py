from langchain_community.document_loaders import DirectoryLoader, TextLoader

DATA_PATH = "data"

loader = DirectoryLoader(
    DATA_PATH,
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents")

for document in documents:
    print(document.metadata["source"])