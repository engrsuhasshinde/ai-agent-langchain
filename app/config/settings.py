from pydantic import Field  # Use 'Field' for defaults so that app works even if .env is empty
from pydantic_settings import BaseSettings, SettingsConfigDict  # 'SettingsConfigDict' is the modern (Pydantic v2) way to handle .env files

class Settings(BaseSettings):
    BASE_URL: str
    API_KEY: str

    LLM_MODEL: str
    EMBEDDING_MODEL: str

    CHROMA_DB_PATH: str
    COLLECTION_NAME: str

    CHUNK_SIZE: int
    TOP_K: int
    SIMILARITY_THRESHOLD: float

    SYSTEM_PROMPT: str

    class Config:
        env_file = ".env"

settings = Settings()