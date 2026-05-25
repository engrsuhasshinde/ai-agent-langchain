from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config.settings import settings

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap  = 50,  # 50 characters of overlap between chunks
    separators = ["\n\n", "\n", ". ", " ", ""],  # tries each separator before splitting
    length_function = len  # uses built-in len function to calculate the length of text chunks
)

def split_text(text: str) -> list[str]:
    return text_splitter.split_text(text)