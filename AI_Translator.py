from googletrans import Translator
from gtts import gTTS

def translate_text(text, target_language_code, source_language_code=None):
    translator = Translator()
    translation = translator.translate(text, dest=target_language_code, src=source_language_code)
    return translation.text

def read_aloud(text, lang):
    """
    Generates speech from text and saves it as an audio file.

    Args:
        text (str): The text to be read aloud.
        lang (str): The language code for the text.
    """
    tts = gTTS(text=text, lang=lang)
    tts.save("translated_audio.mp3")


import googletrans
supported_languages = googletrans.LANGUAGES

text_to_translate = input("Enter the text you want to translate: ")

source_language_input = input("\nTranslate From: ")
target_language_input = input("Translate To: ")

source_language_code = None
if source_language_input:
    if source_language_input in supported_languages:
        source_language_code = source_language_input
    else:
        for code, lang in supported_languages.items():
            if lang.lower() == source_language_input.lower():
                source_language_code = code
                break
    if not source_language_code:
        print("\nSorry, the source language you entered is not supported. Attempting with auto-detection.")


target_language_code = None
if target_language_input in supported_languages:
    target_language_code = target_language_input
else:
    for code, lang in supported_languages.items():
        if lang.lower() == target_language_input.lower():
            target_language_code = code
            break

if target_language_code:
    translated_text = translate_text(text_to_translate, target_language_code, source_language_code)
    print(f"\nTranslated text ({target_language_input}): {translated_text}")
    read_aloud(translated_text, target_language_code)
else:
    print("\nSorry, the target language you entered is not supported.")