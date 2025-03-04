"""Functions to translate between French and English"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate English to French"""
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate French to English."""
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
