import re
import math
from word2number import w2n

def text_to_number(text):
    """Converts text-based numbers into digits."""
    try:
        return w2n.word_to_num(text)
    except ValueError:
        return None  # If conversion fails, return None

def solve_math(expression):
    """Extracts numbers and operators to calculate the result."""
    
    # Convert words to numbers
    words_to_replace = re.findall(r'\b[a-zA-Z]+\b', expression)
    
    for word in words_to_replace:
        number = text_to_number(word)
        if number is not None:
            expression = expression.replace(word, str(number))

    # Handle square roots
    if "square root of" in expression:
        number = re.search(r"\d+", expression)
        if number:
            return math.sqrt(int(number.group()))
    
    # Handle exponents
    if "to the power of" in expression:
        numbers = re.findall(r"\d+", expression)
        if len(numbers) == 2:
            return int(numbers[0]) ** int(numbers[1])
    
    # Evaluate the mathematical expression
    try:
        return eval(expression)  # WARNING: Only use eval in controlled environments
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return None  # Return None for non-math inputs