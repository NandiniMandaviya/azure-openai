from src.components.parsing import run_parse_and_chunk
from src.components.creating_v_db import run_add_to_chroma_db
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from src.retrieval import query_and_rerank_chroma_db

if __name__ == "__main__":
    #run_parse_and_chunk()
    #run_add_to_chroma_db()
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path="./LNTRAG_CHROMADB")
    collection = client.get_or_create_collection(name="LNT_COLLECTION")
    cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    print("Hello user, what would you like to know?")
    query = input()

    relevant_content = query_and_rerank_chroma_db(cross_encoder, model, collection, query, 3)
    print(relevant_content)
