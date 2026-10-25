from pathlib import Path
import re
from pypdf import PdfReader

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


def load_pdfs(data_dir=DATA_DIR):
    documents = []
    pdf_files = sorted(data_dir.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in: {data_dir}. "
            "Copy your PDF files into the data folder."
        )

    for pdf_path in pdf_files:
        reader = PdfReader(str(pdf_path))

        match = re.search(r"20\d{2}", pdf_path.name)
        year = match.group(0) if match else "N/A"

        for page_number, page in enumerate(reader.pages, start=1):
            text = " ".join((page.extract_text() or "").split())

            if not text:
                continue

            documents.append({
                "text": text,
                "metadata": {
                    "source": pdf_path.name,
                    "page": page_number,
                    "year": year,
                },
            })

    return documents


if __name__ == "__main__":
    pages = load_pdfs()
    print(f"Successfully extracted {len(pages)} PDF pages.")

    for page in pages[:5]:
        print(
            f"\nFile: {page['metadata']['source']} | "
            f"Page: {page['metadata']['page']}"
        )
        print(page["text"][:250])
