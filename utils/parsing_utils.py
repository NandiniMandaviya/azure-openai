import requests
from bs4 import BeautifulSoup
from pathlib import Path
from PyPDF2 import PdfReader


DATASETS_DIR = Path("datasets")
DATASETS_DIR.mkdir(parents=True, exist_ok=True)


def save_webpages_as_text(urls):

    for url, filename in urls.items():

        try:
            print(f"Fetching content from: {url}")

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            print(f"Parsing content from: {url}")

            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)

            file_path = DATASETS_DIR / filename

            print(f"Saving content to: {file_path}")

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)

            print(
                f"Successfully saved content from "
                f"{url} to {filename}\n"
            )

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")


def download_and_parse_pdfs(pdf_urls):

    for url, filename in pdf_urls.items():

        pdf_filepath = DATASETS_DIR / filename

        txt_filename = filename.replace(".pdf", ".txt")
        txt_filepath = DATASETS_DIR / txt_filename

        try:
            print(f"Downloading PDF from: {url}")

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            print(f"Saving PDF to: {pdf_filepath}")

            with open(pdf_filepath, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            print(
                f"Successfully downloaded PDF "
                f"from {url} to {pdf_filepath}"
            )

            print(f"Extracting text from PDF: {pdf_filepath}")

            with open(pdf_filepath, "rb") as pdf_file:

                pdf_reader = PdfReader(pdf_file)

                extracted_text = "\n".join(
                    page.extract_text() or ""
                    for page in pdf_reader.pages
                )

            print(f"Saving parsed text to: {txt_filepath}")

            with open(txt_filepath, "w", encoding="utf-8") as file:
                file.write(extracted_text)

            print(
                f"Successfully saved parsed content "
                f"from {url} to {txt_filepath}\n"
            )

        except Exception as e:
            print(f"Error parsing PDF from {url}: {e}")


def process_text_files(urls):

    pdf_urls = {
        url: filename
        for url, filename in urls.items()
        if filename.endswith(".pdf")
    }

    webpage_urls = {
        url: filename
        for url, filename in urls.items()
        if not filename.endswith(".pdf")
    }

    if pdf_urls:
        print(f"Processing {len(pdf_urls)} PDF URLs...")
        download_and_parse_pdfs(pdf_urls)

    if webpage_urls:
        print(f"Processing {len(webpage_urls)} Webpage URLs...")
        save_webpages_as_text(webpage_urls)