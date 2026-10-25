def chunk_documents(documents, chunk_size=1000, overlap=150):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk settings.")

    chunks = []
    step = chunk_size - overlap

    for doc in documents:
        text = doc["text"]
        metadata = doc["metadata"]

        for index, start in enumerate(range(0, len(text), step)):
            passage = text[start:start + chunk_size]
            if passage.strip():
                chunks.append({
                    "id": f"{metadata['source']}_p{metadata['page']}_c{index}",
                    "text": passage,
                    "metadata": metadata.copy(),
                })

    return chunks
