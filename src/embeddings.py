import ollama

EMBED_MODEL = "nomic-embed-text:latest"

def embed_documents(texts):
    if not texts:
        return []
    result = ollama.embed(
        model=EMBED_MODEL,
        input=[f"search_document: {text}" for text in texts],
    )
    return result.embeddings

def embed_query(question):
    result = ollama.embed(
        model=EMBED_MODEL,
        input=[f"search_query: {question}"],
    )
    return result.embeddings[0]
