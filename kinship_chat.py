from googletrans import Translator


def return_text_kinship(file_path, start_line=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        if start_line is not None:
            lines = lines[start_line:]
        last_lines = lines[-6:]

    messages = []

    for line in last_lines:
        if '[To Kinship]' in line or 'has come online.' in line or 'has come offline.' in line:
            continue

        parts = line.split('] ', 1)

        if len(parts) > 1:
            timestamp = parts[0].strip('[] ')
            player_message = parts[1].strip().strip("'")

            messages.append((timestamp, player_message))

    return messages


def translate_messages_kinship(lang, messages, processed_timestamps):
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
