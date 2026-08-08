def query_chroma_db(embedding_model, collection, query, top_k=5):

    print(f"Fetching top {top_k} relevant queries for '{query}'")

    # Convert query into an embedding
    print("Generating embedding for the query...")
    query_embedding = embedding_model.encode(
        [query],
        show_progress_bar=False
    )

    # Perform similarity search
    print("Performing similarity search in ChromaDB collection...")

    search_results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    # Chroma returns nested lists because multiple queries can be supplied
    documents = search_results["documents"][0]
    metadatas = search_results["metadatas"][0]
    distances = search_results["distances"][0]

    relevant_queries = [
        {
            "document": doc,
            "metadata": metadatas[index],
            "score": distances[index]
        }
        for index, doc in enumerate(documents)
    ]

    print(
        f"Found {len(relevant_queries)} relevant documents "
        f"based on embedding similarity."
    )

    return relevant_queries


def query_and_rerank_chroma_db(
    cross_encoder,
    embedding_model,
    collection,
    query,
    top_k=5
):

    print(f"Getting top {top_k} most relevant content for query: {query}")

    # First pass: embedding similarity search
    print("First Pass: Fetching query results using embedding similarity.")

    top_results = query_chroma_db(
        embedding_model,
        collection,
        query,
        top_k
    )

    # Second pass: CrossEncoder reranking
    print("Second Pass: Re-ranking candidates using cross-encoder.")

    ranked_results = []

    for result in top_results:

        cross_encoder_score = cross_encoder.predict(
            [(query, result["document"])]
        )[0]

        ranked_results.append({
            "document": result["document"],
            "metadata": result["metadata"],
            "similarity_score": result["score"],
            "cross_encoder_score": cross_encoder_score
        })

    # Sort by CrossEncoder score
    sorted_results = sorted(
        ranked_results,
        key=lambda x: x["cross_encoder_score"],
        reverse=True
    )[:top_k]

    print(
        f"Retrieved final {len(sorted_results)} "
        f"most relevant content items after re-ranking."
    )

    return sorted_results