from app.core.llm import client
from app.config.settings import settings

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model=settings.EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding