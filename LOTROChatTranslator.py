from googletrans import Translator
import time
import os
import ctypes
import warnings

warnings.filterwarnings("ignore", ".*64-bit application should be automated using 64-bit Python.*")

ctypes.windll.kernel32.SetConsoleTitleW("LOTRO Chat Translator")


def return_text(file_path, start_line=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        if start_line is not None:
            lines = lines[start_line:]
        last_lines = lines[-10:]

    messages = []

    for line in last_lines:
        if '[To World]' in line:
            continue

        parts = line.split('] ', 1)

        if len(parts) > 1:
            timestamp = parts[0].strip('[] ')
            player_message = parts[1].strip().strip("'")

            messages.append((timestamp, player_message))

    return messages


def translate_messages(lang, messages, processed_timestamps):
    playername = ''
    text = ''

    translator = Translator(service_urls=['translate.googleapis.com'])
    new_translations = []

    for timestamp, message in messages:
        if timestamp not in processed_timestamps:
            if ': ' in message:
                playername, text = message.split(': ', 1)

            x = translator.translate(text, dest=lang)
            translated_message = f"[{timestamp}] {playername}: {x.text}'"
            processed_timestamps.add(timestamp)
            new_translations.append(translated_message)

    return new_translations


def main():
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

    while True:
        messages = return_text(path)

        new_translations = translate_messages(lang, messages, processed_timestamps)

        for msg in new_translations:
            print(msg)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
