def learn_new_response(user_input):
    """Asks the user to teach the chatbot a new response."""
    print(f"Chatbot: I don't know how to respond to '{user_input}'. Can you teach me?")
    new_response = input("You: ")
    return new_response