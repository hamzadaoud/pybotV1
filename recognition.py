import re

def recognize_input(user_input):
    """Classifies the input as a number, word, or unknown."""
    
    if re.fullmatch(r"\d+", user_input):  # Detects pure numbers
        return "number"
    elif re.fullmatch(r"[a-zA-Z\s]+", user_input):  # Detects pure words
        return "word"
    else:
        return "unknown"