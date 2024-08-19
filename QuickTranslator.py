from googletrans import Translator
import pyperclip
import os
import ctypes
import warnings

warnings.filterwarnings("ignore", ".*64-bit application should be automated using 64-bit Python.*")

ctypes.windll.kernel32.SetConsoleTitleW("Quick Translator")


def translate_my_message(text, lang):
    translator = Translator(service_urls=['translate.googleapis.com'])
    x = translator.translate(text, dest=lang)
    os.system('cls')
    print("Your message was translated to:")
    print("")
    print(x.text)
    print("")
    print("Paste it to your in-game chat, and send to your foreign friend :)")
    print("")
    pyperclip.copy(x.text)


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

ctypes.windll.kernel32.SetConsoleTitleW(f"Now translating your messages to: {lang}")

while True:
    text = input("Type your message: ")
    translate_my_message(text, lang)
