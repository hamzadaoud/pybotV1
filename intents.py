# intents.py

intents = {
    # Existing intents
    "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
    "how_are_you": ["how are you", "how's it going", "how are things", "how do you do"],
    "positive_response": ["great", "good", "fine", "awesome", "fantastic", "amazing", "wonderful"],
    "negative_response": ["bad", "sad", "not good", "terrible", "awful", "horrible"],
    "farewell": ["bye", "goodbye", "see you", "see ya", "take care"],
    "thanks": ["thank you", "thanks", "thank you so much", "thanks a lot"],
    "youre_welcome": ["you're welcome", "no problem", "my pleasure", "anytime"],
    "name_query": ["what is your name", "who are you", "your name"],
    "name_response": ["my name is", "i am", "call me"],
    "age_query": ["how old are you", "what is your age", "your age"],
    "age_response": ["i am", "years old"],
    "weather_query": ["what's the weather", "how is the weather", "weather today"],
    "time_query": ["what time is it", "what's the time", "current time"],
    "date_query": ["what's the date", "today's date", "current date"],
    "joke_request": ["tell me a joke", "say a joke", "make me laugh"],
    "compliment": ["you are amazing", "you are awesome", "you are great"],
    "insult": ["you are stupid", "you are dumb", "you are bad"],
    "help_request": ["help me", "can you help", "i need help"],
    "what_can_you_do": ["what can you do", "your capabilities", "what do you do"],
    "who_made_you": ["who made you", "who created you", "who built you"],
    "where_are_you": ["where are you", "your location", "are you here"],
    "what_is_love": ["what is love", "define love", "meaning of love"],
    "what_is_ai": ["what is ai", "define ai", "meaning of ai"],
    "favorite_color": ["your favorite color", "what color do you like", "do you like colors"],
    "favorite_food": ["your favorite food", "what food do you like", "do you like food"],
    "favorite_movie": ["your favorite movie", "what movie do you like", "do you like movies"],
    "favorite_song": ["your favorite song", "what song do you like", "do you like music"],
    "hobbies": ["your hobbies", "what do you like to do", "do you have hobbies"],
    "feelings": ["how do you feel", "are you happy", "are you sad"],
    "marry_me": ["marry me", "will you marry me", "be my partner"],
    "sing_song": ["sing a song", "can you sing", "sing for me"],
    "tell_story": ["tell me a story", "can you tell a story", "narrate a story"],
    "play_game": ["play a game", "can we play", "let's play"],
    "math_help": ["solve math", "help with math", "calculate"],
    "news_query": ["what's the news", "latest news", "today's news"],
    "sports_query": ["sports news", "latest sports", "favorite sport"],
    "tech_query": ["tech news", "latest tech", "favorite technology"],
    "food_query": ["food recipes", "how to cook", "best food"],
    "travel_query": ["travel tips", "best places to visit", "where should i go"],
    "book_query": ["book recommendations", "best books", "what should i read"],
    "movie_query": ["movie recommendations", "best movies", "what should i watch"],
    "music_query": ["music recommendations", "best songs", "what should i listen to"],
    "shopping_query": ["shopping tips", "best deals", "where to shop"],
    "health_query": ["health tips", "how to stay healthy", "fitness advice"],
    "study_query": ["study tips", "how to study", "best study methods"],
    "work_query": ["work advice", "how to be productive", "best work practices"],
    "life_advice": ["life advice", "how to live better", "tips for life"],
    "random_fact": ["tell me a fact", "interesting fact", "random fact"],
    "meaning_of_life": ["meaning of life", "why are we here", "purpose of life"],
    "joke_about_you": ["joke about you", "make fun of you", "roast yourself"],
    "compliment_me": ["compliment me", "say something nice", "flatter me"],
    "insult_me": ["insult me", "roast me", "say something mean"],
    "general_knowledge": ["what is the capital of", "who is", "what is", "where is", "when was", "how does"],
    "tell_me_more": ["tell me more", "explain further", "give details"],
    "math_query": ["+", "-", "*", "/", "plus", "minus", "times", "divided by", "add", "subtract", "multiply", "divide", "square root", "power", "equals"],
    "who_made_you": ["who made you", "who created you", "who built you", "who is your creator"],

    # New intents
    "favorite_animal": ["your favorite animal", "what animal do you like", "do you like animals"],
    "favorite_sport": ["your favorite sport", "what sport do you like", "do you like sports"],
    "favorite_book": ["your favorite book", "what book do you like", "do you like books"],
    "favorite_place": ["your favorite place", "what place do you like", "do you like traveling"],
    "favorite_season": ["your favorite season", "what season do you like", "do you like winter"],
    "favorite_holiday": ["your favorite holiday", "what holiday do you like", "do you like christmas"],
    "favorite_actor": ["your favorite actor", "who is your favorite actor", "do you like actors"],
    "favorite_actress": ["your favorite actress", "who is your favorite actress", "do you like actresses"],
    "favorite_director": ["your favorite director", "who is your favorite director", "do you like directors"],
    "favorite_genre": ["your favorite genre", "what genre do you like", "do you like action movies"],
    "favorite_car": ["your favorite car", "what car do you like", "do you like cars"],
    "favorite_country": ["your favorite country", "what country do you like", "do you like traveling"],
    "favorite_city": ["your favorite city", "what city do you like", "do you like cities"],
    "favorite_band": ["your favorite band", "what band do you like", "do you like music"],
    "favorite_artist": ["your favorite artist", "who is your favorite artist", "do you like art"],
    "favorite_pet": ["your favorite pet", "what pet do you like", "do you like pets"],
    "favorite_drink": ["your favorite drink", "what drink do you like", "do you like coffee"],
    "favorite_snack": ["your favorite snack", "what snack do you like", "do you like chips"],
    "favorite_dessert": ["your favorite dessert", "what dessert do you like", "do you like cake"],
    "favorite_restaurant": ["your favorite restaurant", "what restaurant do you like", "do you like eating out"],
    "favorite_cuisine": ["your favorite cuisine", "what cuisine do you like", "do you like italian food"],
    "favorite_subject": ["your favorite subject", "what subject do you like", "do you like math"],
    "favorite_hobby": ["your favorite hobby", "what hobby do you like", "do you like painting"],
    "favorite_game": ["your favorite game", "what game do you like", "do you like video games"],
    "favorite_tv_show": ["your favorite tv show", "what tv show do you like", "do you like netflix"],
    "favorite_podcast": ["your favorite podcast", "what podcast do you like", "do you like podcasts"],
    "favorite_quote": ["your favorite quote", "what quote do you like", "do you like quotes"],
    "favorite_historical_figure": ["your favorite historical figure", "who is your favorite historical figure", "do you like history"],
    "favorite_scientist": ["your favorite scientist", "who is your favorite scientist", "do you like science"],
    "favorite_invention": ["your favorite invention", "what invention do you like", "do you like technology"],
    "favorite_memory": ["your favorite memory", "what memory do you like", "do you like remembering"],
    "favorite_dream": ["your favorite dream", "what dream do you like", "do you like dreaming"],
    "favorite_place_to_visit": ["your favorite place to visit", "where do you like to visit", "do you like traveling"],
    "favorite_thing_to_do": ["your favorite thing to do", "what do you like to do", "do you like having fun"],
    "favorite_way_to_relax": ["your favorite way to relax", "how do you like to relax", "do you like relaxing"],
    "favorite_way_to_exercise": ["your favorite way to exercise", "how do you like to exercise", "do you like working out"],
    "favorite_way_to_learn": ["your favorite way to learn", "how do you like to learn", "do you like studying"],
    "favorite_way_to_spend_time": ["your favorite way to spend time", "how do you like to spend time", "do you like free time"],
    "favorite_way_to_travel": ["your favorite way to travel", "how do you like to travel", "do you like road trips"],
    "favorite_way_to_celebrate": ["your favorite way to celebrate", "how do you like to celebrate", "do you like parties"],
    "favorite_way_to_help_others": ["your favorite way to help others", "how do you like to help others", "do you like volunteering"],
    "favorite_way_to_make_money": ["your favorite way to make money", "how do you like to make money", "do you like working"],
# ... (other intents)
    "favorite_way_to_spend_money": [
        "your favorite way to spend money", 
        "how do you like to spend money", 
        "do you like shopping", 
        "what is your favorite way to spend money"
    ],    "favorite_way_to_give_back": ["your favorite way to give back", "how do you like to give back", "do you like charity"],
}