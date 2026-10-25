from src.embeddings import embed_query
from src.vector_store import get_client, COLLECTION_NAME

def retrieve(question, top_k=5):
    client = get_client()

    try:
        collection = client.get_collection(COLLECTION_NAME)
    except Exception as exc:
        raise RuntimeError("Knowledge base missing. Run python ingest.py first.") from exc

    count = collection.count()
    if count == 0:
        return []

    vector = embed_query(question)
    result = collection.query(
        query_embeddings=[vector],
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"],
    )

    return [
        {"text": text, "metadata": meta, "distance": float(distance)}
        for text, meta, distance in zip(
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        )
    ]
