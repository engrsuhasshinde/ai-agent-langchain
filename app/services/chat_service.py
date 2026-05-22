from app.core.llm import client
from app.core.memory import conversation_history
from app.core.vectorstore import collection
from app.core.embeddings import get_embedding
from app.utils.text_chunker import split_into_chunks
from app.config.settings import settings
from app.chains.rag_chain import prepare_rag_prompt

message_counter = 0

def save_message(
        message_id: str,
        role: str,
        text: str
):
    chunks = split_into_chunks(text)

    for index, chunk in enumerate(chunks):
        chunk_id = f"{message_id}_chunk_{index}"
        embedding = get_embedding(chunk)

        collection.upsert(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{ "role": role }]
        )

def process_chat(user_input: str):
    global message_counter
    system_prompt = prepare_rag_prompt(user_input)

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model = settings.LLM_MODEL,
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ] + conversation_history,
        stream = True
    )

    full_response = ""

    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        print(content, end = "", flush = True)
        full_response += content

    print("\n")  # Add a newline after the response is complete

    conversation_history.append({
        "role": "assistant",
        "content": full_response
    })

    save_message(
        f"message_{message_counter}",
        "user",
        user_input
    )

    save_message(
        f"message_{message_counter}",
        "assistant",
        full_response
    )

    message_counter += 1