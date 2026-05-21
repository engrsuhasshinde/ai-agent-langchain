import chromadb
from app.config.settings import settings

db = chromadb.PersistentClient(
    path = settings.CHROMA_DB_PATH
)

collection = db.get_or_create_collection(
    name = settings.COLLECTION_NAME,
    metadata = {
        "hnsw:space": "cosine"
    }
)
