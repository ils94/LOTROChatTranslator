import time
import os
import ctypes
import warnings
import world_chat
import IMs_chat

warnings.filterwarnings("ignore", ".*64-bit application should be automated using 64-bit Python.*")

ctypes.windll.kernel32.SetConsoleTitleW("LOTRO Chat Translator")


def main():
    chat = ''

    while True:
        print("Choose one type of chat to translate:")
        print("")
        print("1- World Chat")
        print("2- IMs")
        print("")
        chat = input("Choice: ")

        os.system('cls')

        if chat == '1' or chat == '2':
            break
        else:
            print("Pick one of the valid choices:")
            print("")

    while True:
        path = input("Paste the path to your chat log: ").strip('"')

        os.system('cls')

        if os.path.isfile(path):
            break
        else:
            print("Invalid file path. Please enter a valid file path.")
            print("")

    # Define supported languages
    supported_languages = {
        'ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'fi',
        'fr', 'ga', 'gl', 'gu', 'he', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'ja',
        'jw', 'kn', 'ko', 'la', 'lv', 'lt', 'mk', 'ml', 'mr', 'my', 'ne', 'no',
        'oc', 'pl', 'pt', 'pa', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn',
        'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tr',
        'uk', 'ur', 'vi', 'xh', 'yi', 'yo', 'zu'
    }

    print("Now pick your desired language to translate")
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

    processed_timestamps = set()
    translated_messages = set()

    while True:
        if chat == '1':
            messages = world_chat.return_text_world(path)
            new_translations = world_chat.translate_messages_world(lang, messages, processed_timestamps)

            for msg in new_translations:
                print(msg)

        elif chat == '2':
            messages = IMs_chat.return_text_ims(path)
            new_translations = IMs_chat.translate_messages_ims(lang, messages, translated_messages)

            for msg in new_translations:
                print(msg)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
