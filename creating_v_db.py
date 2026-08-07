from sentence_transformers import SentenceTransformer
import json
import chromadb


def create_embeddings_from_json(json_filename, model, collection):

    print(
        f"Creating embeddings for chunks in {json_filename} "
        f"using model {model}..."
    )

    # Load chunk data
    with open(json_filename, "r", encoding="utf-8") as file:
        chunks_data = json.load(file)

    # Prepare text and metadata
    sentences = [chunk["chunk"] for chunk in chunks_data]
    metadata = [chunk["metadata"] for chunk in chunks_data]

    # Generate embeddings
    print("Generating embeddings...")

    embeddings = model.encode(sentences)

    # Insert into ChromaDB
    print(
        f"Inserting {len(embeddings)} embeddings "
        f"into the ChromaDB collection..."
    )

    for idx, embedding in enumerate(embeddings):

        collection.add(
            ids=[str(idx)],
            documents=[sentences[idx]],
            metadatas=[metadata[idx]],
            embeddings=[embedding.tolist()]
        )

    print(
        f"Successfully inserted {len(embeddings)} "
        f"embeddings into the ChromaDB collection."
    )


def run_add_to_chroma_db():

    model = SentenceTransformer("all-MiniLM-L6-v2")

    client = chromadb.PersistentClient(
        path="./LNTRAG_CHROMADB"
    )

    collection = client.get_or_create_collection(
        name="LNT_COLLECTION"
    )

    create_embeddings_from_json(
        "datasets/chunks_data.json",
        model,
        collection
    )