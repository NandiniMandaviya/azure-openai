
def query_and_rerank_chroma_db(embedding_model, collection, query, top_k=5):
    print(f"Fetching top {top_k} relevant queries for '{query}'")

    #Converting the query to an embedding
    print("Generating embedding for the query...")
    query_embedding = embedding_model.encode([query], show_progress_bar=False)

    #Perform similarity search in ChromaDB collection
    print("Performing similarity search in ChromaDB collection...")
    search_results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    relevant_queries = [
        {
            "document": doc,
            "metadata": search_results["metadatas"][index],
            "score": search_results["distances"][index]
        }
        for index, doc in enumerate(search_results["documents"])
    ]

    print(f"Found {len(relevant_queries)} relevant documents based on embeddings similarity.")

    return relevant_queries

