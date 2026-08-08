from src.components.parsing import run_parse_and_chunk
from src.components.creating_v_db import run_add_to_chroma_db
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from src.retrieval import query_and_rerank_chroma_db

import os
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

azure_client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

if __name__ == "__main__":
    #run_parse_and_chunk()
    #run_add_to_chroma_db()
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    chromadb_client = chromadb.PersistentClient(path="./LNTRAG_CHROMADB")
    collection = chromadb_client.get_or_create_collection(name="LNT_COLLECTION")
    cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    print("Hello user, what would you like to know?")
    query = input()

    relevant_content = query_and_rerank_chroma_db(cross_encoder, model, collection, query, 3)
    query += f"attached content: {relevant_content}"

    response = azure_client.chat.completions.create(
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Use the attached content if needed."},
            {"role": "user", "content": query},
        ],
        model = deployment,
    )

    print(response.choices[0].message.content)