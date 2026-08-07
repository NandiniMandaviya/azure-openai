import re
import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


def preprocess_text(text, filename, url):

    # Clean excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Create text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=32,
    )

    # Split text
    chunks = text_splitter.split_text(text)

    # Attach metadata
    chunks_data = []

    for chunk in chunks:
        chunks_data.append({
            "chunk": chunk,
            "metadata": {
                "source": filename,
                "url": url
            }
        })

    print(f"Processed {len(chunks)} chunks for {filename} from {url}")

    return chunks_data


def chunk_data(urls):

    all_chunks_data = []

    print("Starting to process text files and chunk data...")

    for url, filename in urls.items():

        # PDFs have already been converted to TXT
        if filename.endswith(".pdf"):
            filename = filename.replace(".pdf", ".txt")

        try:
            print(f"Processing text file: {filename} from URL: {url}")

            file_path = Path("datasets") / filename

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            chunks_data = preprocess_text(
                text,
                filename,
                url
            )

            all_chunks_data += chunks_data

            print(
                f"Added {len(chunks_data)} chunks "
                f"from {filename} to knowledge base."
            )

        except Exception as e:
            print(
                f"Error processing {filename} "
                f"from {url}: {e}"
            )

    print(
        f"Saved a total of {len(all_chunks_data)} chunks "
        f"from all text files to JSON file."
    )

    output_path = Path("datasets") / "chunks_data.json"

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(
            all_chunks_data,
            json_file,
            ensure_ascii=False,
            indent=4
        )

    print(
        "Successfully saved all chunks data "
        "to 'datasets/chunks_data.json'."
    )