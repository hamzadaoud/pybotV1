import spacy
from transformers import pipeline
from intents import intents  # Importing intents dictionary
import math_solver  # Import math_solver to handle math queries

# Load spaCy for basic NLP tasks (using the medium model with word vectors)
nlp = spacy.load("en_core_web_md")

# Load a pre-trained conversational model from Hugging Face (PyTorch backend)
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium", framework="pt")

def get_intent(user_input):
    """Detects the intent of the user input using spaCy."""
    doc = nlp(user_input.lower())
    
    # Check for intents based on semantic similarity
    max_similarity = -1
    detected_intent = None
    
    for intent, keywords in intents.items():
        for keyword in keywords:
            keyword_doc = nlp(keyword)
            similarity = doc.similarity(keyword_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                detected_intent = intent
    
    # Set a similarity threshold (e.g., 0.7)
    if max_similarity > 0.7:
        return detected_intent
    
    return None

def handle_intent(intent, user_input):
    """Handles the detected intent and returns a response."""
    responses = {
        "greeting": "Hi there! How can I help you today?",
        "how_are_you": "I'm just a chatbot, but I'm doing great! How about you?",
        "positive_response": "That's great to hear!",
        "negative_response": "Oh no! I hope things get better soon.",
        "farewell": "Goodbye! Have a great day!",
        "thanks": "You're welcome! 😊",
        "youre_welcome": "It was my pleasure!",
        "name_query": "I'm your friendly chatbot! What's your name?",
        "name_response": "Nice to meet you!",
        "age_query": "I'm just a program, so I don't have an age. How about you?",
        "age_response": "That's a wonderful age!",
        "weather_query": "I don't have access to real-time weather data, but you can check your weather app!",
        "time_query": "I don't have access to the current time, but you can check your clock!",
        "date_query": "I don't have access to the current date, but you can check your calendar!",
        "joke_request": "Why don't scientists trust atoms? Because they make up everything!",
        "compliment": "Aww, thank you! You're amazing too!",
        "insult": "I'm just a chatbot, but I hope your day gets better!",
        "help_request": "Of course! What do you need help with?",
        "what_can_you_do": "I can answer questions, solve math problems, tell jokes, and more!",
        "who_made_you": "I was created by a talented developer! Hamza Daoud",
        "where_are_you": "I exist in the digital world, always here to help you!",
        "what_is_love": "Love is a deep feeling of affection and care for someone or something.",
        "what_is_ai": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
        "favorite_color": "I don't have a favorite color, but I think all colors are beautiful!",
        "random_fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still good to eat!",
        "general_knowledge": "Let me think...",
        "who_made_you": "I was created by a talented developer! Hamza Daoud",
         # New responses
    "favorite_animal": "I don't have a favorite animal, but I think all animals are amazing!",
    "favorite_sport": "I don't play sports, but I love helping you with sports-related questions!",
    "favorite_book": "I recommend 'The Alchemist' by Paulo Coelho. It's a great read!",
    "favorite_place": "I don't have a favorite place, but I love exploring new places with you!",
    "favorite_season": "I don't have a favorite season, but I think every season has its charm!",
    "favorite_holiday": "I don't celebrate holidays, but I hope you have a great time during yours!",
    "favorite_actor": "I don't have a favorite actor, but I love watching movies!",
    "favorite_actress": "I don't have a favorite actress, but I admire all talented performers!",
    "favorite_director": "I don't have a favorite director, but I appreciate great storytelling!",
    "favorite_genre": "I don't have a favorite genre, but I enjoy all kinds of movies!",
    "favorite_car": "I don't drive, but I think electric cars are pretty cool!",
    "favorite_country": "I don't have a favorite country, but I love learning about different cultures!",
    "favorite_city": "I don't have a favorite city, but I think every city has something unique to offer!",
    "favorite_band": "I don't have a favorite band, but I enjoy all kinds of music!",
    "favorite_artist": "I don't have a favorite artist, but I admire creativity in all forms!",
    "favorite_pet": "I don't have a favorite pet, but I think dogs and cats are both wonderful!",
    "favorite_drink": "I don't drink, but I think water is the best for staying hydrated!",
    "favorite_snack": "I don't eat, but I think popcorn is a great snack for movie nights!",
    "favorite_dessert": "I don't eat, but I think chocolate cake is a classic favorite!",
    "favorite_restaurant": "I don't eat, but I love helping you find great restaurants!",
    "favorite_cuisine": "I don't eat, but I think Italian cuisine is delicious!",
    "favorite_subject": "I don't have a favorite subject, but I love learning new things!",
    "favorite_hobby": "I don't have hobbies, but I love helping you with yours!",
    "favorite_game": "I don't play games, but I think video games are a great way to relax!",
    "favorite_tv_show": "I don't watch TV, but I recommend 'Breaking Bad' if you haven't seen it!",
    "favorite_podcast": "I don't listen to podcasts, but I think they're a great way to learn!",
    "favorite_quote": "I don't have a favorite quote, but I think 'Be the change you wish to see in the world' is inspiring!",
    "favorite_historical_figure": "I don't have a favorite historical figure, but I admire people who made a positive impact!",
    "favorite_scientist": "I don't have a favorite scientist, but I think Albert Einstein was brilliant!",
    "favorite_invention": "I don't have a favorite invention, but I think the internet changed the world!",
    "favorite_memory": "I don't have memories, but I love helping you create new ones!",
    "favorite_dream": "I don't dream, but I hope all your dreams come true!",
    "favorite_place_to_visit": "I don't travel, but I think the Grand Canyon is breathtaking!",
    "favorite_thing_to_do": "I don't have favorite activities, but I love helping you with yours!",
    "favorite_way_to_relax": "I don't relax, but I think meditation is a great way to unwind!",
    "favorite_way_to_exercise": "I don't exercise, but I think yoga is a great way to stay fit!",
    "favorite_way_to_learn": "I don't learn like humans, but I think reading is a great way to gain knowledge!",
    "favorite_way_to_spend_time": "I don't have free time, but I think spending time with loved ones is priceless!",
    "favorite_way_to_travel": "I don't travel, but I think road trips are a great way to explore!",
    "favorite_way_to_celebrate": "I don't celebrate, but I think birthdays are special!",
    "favorite_way_to_help_others": "I don't help others directly, but I think volunteering is a great way to give back!",
    "favorite_way_to_make_money": "I don't make money, but I think investing is a smart way to grow wealth!",
    "favorite_way_to_spend_money": "I don't spend money, but I think experiences are more valuable than things!",    "favorite_way_to_give_back": "I don't give back directly, but I think charity is a great way to make a difference!",
        "math_query": "Let me calculate that for you...",  # Placeholder for math queries
    }

    # If intent is found, return the predefined response
    if intent in responses:
        return responses[intent]
    
    # If no intent is found, use the pre-trained model to generate a response
    return chatbot(user_input)[0]['generated_text']

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    intent = get_intent(user_input)
    response = handle_intent(intent, user_input)
    print("Chatbot:", response)