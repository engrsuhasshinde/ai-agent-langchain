from app.config.settings import settings

def build_system_prompt(context: str) -> str:
    if not context:
        return settings.SYSTEM_PROMPT

    return f"""
{settings.SYSTEM_PROMPT}

Relevant context from past conversation:

{context}

Use the context above only if it helps answer the question.
"""