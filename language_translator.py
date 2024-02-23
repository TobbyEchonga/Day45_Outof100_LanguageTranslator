from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    # Sample text (replace with your own)
    text_to_translate = "Bonjour, comment Ã§a va?"

    # Target language (replace with the language code of your choice)
    target_language = 'en'

    # Translate the text
    translated_text = translate_text(text_to_translate, target_language)

    # Display the result
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")
