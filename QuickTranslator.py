from googletrans import Translator
import pyperclip
import os
import window_config

window_title = 'Quick Translator'

window_config.window_always_on_top(window_title)


def translate_my_message(text, lang):
    translator = Translator(service_urls=['translate.googleapis.com'])
    x = translator.translate(text, dest=lang)
    os.system('cls')
    print("After your message is translated, you can just Ctrl + V into LOTRO chat!")
    print("")
    print("Your message was translated to:")
    print("")
    print(x.text)
    print("")
    pyperclip.copy(x.text)


def main():
    supported_languages = {
        'ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'fi',
        'fr', 'ga', 'gl', 'gu', 'he', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'ja',
        'jw', 'kn', 'ko', 'la', 'lv', 'lt', 'mk', 'ml', 'mr', 'my', 'ne', 'no',
        'oc', 'pl', 'pt', 'pa', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn',
        'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tr',
        'uk', 'ur', 'vi', 'xh', 'yi', 'yo', 'zu'
    }

    print("Pick one of the available languages to translate your message.")
    print("")
    print("These are the following languages available:")
    print("")
    print(", ".join(supported_languages))
    print("")

    while True:
        lang = input("Desired language: ").strip()

        os.system('cls')

        if lang in supported_languages:
            break
        else:
            print(", ".join(supported_languages))
            print("")
            print("Unsupported language code. Please choose from the list.")
            print("")

    os.system('cls')
    print("After your message is translated, you can just Ctrl + V into LOTRO chat!")
    print("")

    while True:
        text = input("Type your message: ")
        translate_my_message(text, lang)


if __name__ == "__main__":
    main()
