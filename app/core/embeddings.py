from app.core.llm import client
from app.config.settings import settings
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(
    model = settings.EMBEDDING_MODEL,
    openai_api_base = settings.BASE_URL,  # points to local Ollama server
    openai_api_key = settings.API_KEY
)

def get_embedding(text: str) -> list[float]:
    return embeddings_model.embed_query(text)