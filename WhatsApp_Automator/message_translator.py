from translate import Translator
#language = {'en', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'zh-CN', 'zh-TW'}
try:
    input_text = input("What text would you like to translate? ")  # Input text
    output_language = input("What language would you like to translate to? ")  # Desired Output language
    translator= Translator(from_lang='en',to_lang=output_language)
    translation = translator.translate(input_text)
    print(f'Translated text: {translation}: {output_language}')
except Exception as e:
    print(f"An error occurred: {e}")