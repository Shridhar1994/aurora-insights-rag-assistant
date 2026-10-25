from src.pdf_loader import load_pdfs
from src.chunking import chunk_documents
from src.embeddings import embed_documents
from src.vector_store import build_vector_store

def run_ingestion():
    print("Loading PDF pages...")
    documents = load_pdfs()
    print(f"Pages extracted: {len(documents)}")

    print("Splitting into chunks...")
    chunks = chunk_documents(documents)
    print(f"Chunks created: {len(chunks)}")

    print("Generating embeddings with Ollama...")
    vectors = embed_documents([x["text"] for x in chunks])
    print(f"Embeddings created: {len(vectors)}")

    print("Saving to ChromaDB...")
    collection = build_vector_store(chunks, vectors)
    print(f"SUCCESS: Stored {collection.count()} chunks.")
    return collection.count()

if __name__ == "__main__":
    run_ingestion()
