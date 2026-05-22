from app.core.embeddings import get_embedding
from app.core.vectorstore import collection
from app.config.settings import settings

def find_relevant_context(
    query: str,
    top_k: int = settings.TOP_K # Use the default value from settings, but allow it to be overridden
) -> str:

    if collection.count() == 0:
        return ""

    results = collection.query(
        query_embeddings = [get_embedding(query)], # Use the 'get_embedding' function to convert the query into an embedding vector
        n_results = min(top_k, collection.count()),
        include = ["documents", "distances"]
    )

    documents = results['documents'][0] # Get the list of documents from the query results
    distances = results['distances'][0] # Get the list of distances from the query

    relevant_context = []

    for document, distance in zip(documents, distances):
        similarity = 1 - distance # Convert distance to similarity (assuming distance is between 0 and 1)

        if similarity >= settings.SIMILARITY_THRESHOLD: # Use the similarity threshold from settings
            relevant_context.append(document) # If the similarity is above the threshold, add the document to the relevant context

    return "\n".join(relevant_context) # Return the relevant context as a single string