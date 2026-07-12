print("=" * 40)
print("🤖 Welcome to DecodeLabs AI Chatbot")
print("Type 'exit' anytime to end the chat.")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is DecodeBot.")

    elif user == "who made you":
        print("Bot: I was created by an AI Intern at DecodeLabs.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "time":
        from datetime import datetime
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        from datetime import datetime
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")