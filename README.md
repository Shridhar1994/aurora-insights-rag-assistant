# Aurora Insights — Local PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that lets users ask questions about business reports in natural language and receive answers based on retrieved PDF content.

## Features

- PDF document ingestion and text extraction using pypdf
- Text chunking with configurable overlap
- Local embeddings using Ollama and nomic-embed-text
- Persistent vector storage and semantic retrieval using ChromaDB
- Question answering using Llama 3.2
- Streamlit chat interface
- Source filename and page metadata for citation display
- Local model execution without a hosted LLM API

## Architecture

```text
PDF Reports
    |
    v
PDF Text Extraction (pypdf)
    |
    v
Text Chunking
    |
    v
Embedding Generation (Ollama)
    |
    v
ChromaDB Vector Store
    |
    v
User Question --> Query Embedding
                       |
                       v
                Similarity Search
                       |
                       v
                Relevant Passages
                       |
                       v
                Ollama LLM
                       |
                       v
              Answer + Citations
                       |
                       v
                  Streamlit UI
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| Ollama | Local language model and embeddings |
| Llama 3.2 | Answer generation |
| nomic-embed-text | Text embeddings |
| ChromaDB | Vector database |
| pypdf | PDF extraction |
| Git and GitHub | Version control |

## Project Structure

```text
Aurora_RAG_App/
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
└── src/
    ├── pdf_loader.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retriever.py
    └── rag_chain.py
```

## Prerequisites

- Python 3.10 or newer, compatible with the installed dependencies
- Git
- Ollama installed and running

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Shridhar1994/aurora-insights-rag-assistant.git
cd aurora-insights-rag-assistant
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Download the required Ollama models

```powershell
ollama pull llama3.2
ollama pull nomic-embed-text
```

Ensure Ollama is running before continuing.

### 5. Add PDF documents

Place the PDF documents you are permitted to use in the `data/` directory.

### 6. Build the knowledge base

```powershell
python ingest.py
```

### 7. Launch the application

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Example Questions

Try questions whose answers appear in your loaded reports:

- What was the reported revenue in FY2025?
- How did net debt change between FY2024 and FY2025?
- Which business segment had the highest revenue growth?
- What revenue target was stated in the outlook?

Verify answers against the original documents during testing.

## Engineering Notes

- The vector database is generated locally during ingestion.
- Initial ingestion can take time while embeddings are generated.
- Ollama must have the required models available.
- Source metadata supports citation display; citation accuracy and handling of unsupported questions should be tested.
- This is a local prototype, not yet a production-hardened deployment.

## Future Enhancements

- Automated tests and answer-quality evaluation
- Retrieval relevance thresholds and improved refusal handling
- Docker containerization
- GitHub Actions CI/CD
- AWS deployment with security, logging, and monitoring

## Author

Built as a hands-on GenAI and RAG engineering project.
