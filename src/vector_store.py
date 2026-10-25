from pathlib import Path
import chromadb

PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_DIR / "data" / "chroma_db"
COLLECTION_NAME = "aurora_reports"

def get_client():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(DB_DIR))

def build_vector_store(chunks, embeddings):
    if not chunks or len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must both be present and match.")

    client = get_client()

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    for start in range(0, len(chunks), 100):
        batch = chunks[start:start + 100]
        vectors = embeddings[start:start + 100]

        collection.add(
            ids=[x["id"] for x in batch],
            documents=[x["text"] for x in batch],
            embeddings=[
                v.tolist() if hasattr(v, "tolist") else list(v)
                for v in vectors
            ],
            metadatas=[x["metadata"] for x in batch],
        )

    return collection
