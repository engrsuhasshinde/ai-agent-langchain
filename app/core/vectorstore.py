from langchain_chroma import Chroma
from app.core.embeddings import embeddings_model
from app.config.settings import settings

# Chroma from LangChain wraps the raw client
# Handles: ID generation, embedding calls, upsert - all in one method

vectorstore = Chroma(
    collection_name = settings.COLLECTION_NAME,
    embedding_function = embeddings_model,
    persist_directory = settings.CHROMA_DB_PATH,
    collection_metadata = { "hnsw:space": "cosine" }  # Optional: specify the distance metric for HNSW index (e.g., "cosine", "euclidean", "dot_product"
)
