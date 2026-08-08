from datetime import datetime

def save_chat(base_prompt, query, context, response):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 80 + "\n")
        file.write(f"Timestamp: {datetime.now()}\n")
        file.write("=" * 80 + "\n\n")

        file.write("BASE PROMPT:\n")
        file.write(base_prompt + "\n\n")

        file.write("USER QUERY:\n")
        file.write(query + "\n\n")

        file.write("RETRIEVED CONTEXT:\n")
        file.write(context + "\n\n")

        file.write("MODEL RESPONSE:\n")
        file.write(response + "\n\n")