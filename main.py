import json
import response_handler
import learning
from intent_handler import handle_intent, get_intent  # Import updated functions

def load_knowledge():
    """Loads existing knowledge from a file."""
    try:
        with open("knowledge_base.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_knowledge(knowledge):
    """Saves the chatbot's knowledge."""
    with open("knowledge_base.json", "w") as file:
        json.dump(knowledge, file, indent=4)

def main():
    knowledge = load_knowledge()
    print("Chatbot: Hello! Ask me anything. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Check if the response is in the knowledge base
        if user_input in knowledge:
            print(f"Chatbot: {knowledge[user_input]}")
        else:
            # Use intent handling and pre-trained model for unknown inputs
            intent = get_intent(user_input)
            response = handle_intent(intent, user_input)
            print(f"Chatbot: {response}")

            # If the chatbot doesn't know the answer, ask the user to teach it
            if intent is None:
                new_response = learning.learn_new_response(user_input)
                knowledge[user_input] = new_response
                save_knowledge(knowledge)
                print("Chatbot: Thanks! I just learned something new.")

if __name__ == "__main__":
    main()