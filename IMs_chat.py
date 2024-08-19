from googletrans import Translator


def return_text_ims(file_path, start_line=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        if start_line is not None:
            lines = lines[start_line:]
        last_lines = lines[-10:]

    messages = []

    for line in last_lines:
        parts = line.split('] ', 1)

        if len(parts) > 1:
            timestamp = parts[0].strip('[] ')
            player_message = parts[1].strip().strip("'")

            messages.append((timestamp, player_message))

    return messages


def translate_messages_ims(lang, messages, translated_messages):
    new_translations = []
    translator = Translator(service_urls=['translate.googleapis.com'])

    for timestamp, message in messages:
        if message not in translated_messages:
            if ': ' in message:
                playername, text = message.split(': ', 1)
                translated_text = translator.translate(text, dest=lang).text
                translated_message = f"[{timestamp}] {playername}: {translated_text}"
                new_translations.append(translated_message)
                translated_messages.add(message)

    return new_translations
