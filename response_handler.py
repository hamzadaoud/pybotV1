import recognition
import math_solver
import intent_handler

def get_response(user_input, knowledge):
    """Processes user input and returns a response."""

    # Check if chatbot already knows the answer
    if user_input in knowledge:
        return knowledge[user_input]

    # Check for intents using spaCy
    intent = intent_handler.get_intent(user_input)
    if intent:
        return intent_handler.handle_intent(intent, user_input)

    # Recognize numbers or words
    input_type = recognition.recognize_input(user_input)
    if input_type == "number":
        return f"You entered a number: {user_input}"
    elif input_type == "word":
        return f"That seems like a word: {user_input}"

    # Check if input is a math question
    if is_math_question(user_input):
        result = math_solver.solve_math(user_input)
        if result is not None:
            return f"The answer is: {result}"

    # Check if input is a comparison question
    comparison_result = math_solver.solve_comparison(user_input)
    if comparison_result is not None:
        return comparison_result

    # If no response is found, ask the user to teach the chatbot
    return None

def is_math_question(user_input):
    """Checks if the input is likely a math question."""
    math_keywords = ["+", "-", "*", "/", "plus", "minus", "times", "divide", "square root", "power", "equals"]
    return any(keyword in user_input for keyword in math_keywords)