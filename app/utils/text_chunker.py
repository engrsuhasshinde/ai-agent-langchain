import re
from app.config.settings import settings

def split_into_chunks(
    text: str,
    max_words: int = settings.CHUNK_SIZE
) -> list[str]:

    # Split the text into sentences using regex
    sentences = re.split( r'(? <= [.!?]) +', text.strip())

    # Remove any empty sentences
    sentences = [s for s in sentences if s.strip()]

    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        word_count = len(sentence.split())

        # Start a new chunk if adding the current sentence exceeds the max word limit
        if (
            current_word_count + word_count > max_words
            and current_chunk
        ):
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_word_count = 0

        current_chunk.append(sentence)
        current_word_count += word_count

    # Append any remaining text as the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks