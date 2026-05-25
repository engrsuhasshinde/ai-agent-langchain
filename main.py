from app.services.chat_service import process_chat

print("Suhas's Coding Assistant (🤖): Hello!")
print("=" * 50)

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ["exit", "quit"]:
        print("Suhas's Coding Assistant (🤖): Goodbye!")
        break

    try:
        print("\n🤖: ", end="", flush=True)

        process_chat(user_input)
    except Exception as error:
        print(f"\nAn error occurred: {error}")