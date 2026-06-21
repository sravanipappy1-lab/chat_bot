def chatbot():
    print("🤖 Chatbot: Hello! Type something (type 'bye' to exit)")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi!")
        
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        elif user == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()