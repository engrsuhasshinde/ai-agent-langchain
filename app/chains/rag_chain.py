from app.core.retriever import find_relevant_context
from app.prompts.chat_prompt import build_system_prompt

def prepare_rag_prompt(user_input: str) -> str:
    context = find_relevant_context(user_input)
    system_prompt = build_system_prompt(context)
    return system_prompt