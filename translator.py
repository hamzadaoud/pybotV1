from deep_translator import GoogleTranslator

def translate(text, target_language="en"):
    """Translates text to the target language (default is English)."""
    return GoogleTranslator(source="auto", target=target_language).translate(text)