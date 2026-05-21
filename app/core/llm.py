from openai import OpenAI
from app.config.settings import settings

client = OpenAI(
    base_url = settings.BASE_URL,
    api_key = settings.API_KEY
)