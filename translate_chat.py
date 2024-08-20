import common_chat
import ims_chat
import time


def translate(chat_type, text, path, lang, stop_event):
    processed_timestamps = set()
    translated_messages = set()

    while not stop_event.is_set():
        try:
            if chat_type == 'Common Chat':
                messages = common_chat.return_text(path)
                new_translations = common_chat.translate_messages(lang, messages,
                                                                  processed_timestamps)
            elif chat_type == 'IMs Chat':
                messages = ims_chat.return_text(path)
                new_translations = ims_chat.translate_messages(lang, messages, translated_messages)
            else:
                continue

            text.configure(state='normal')

            for msg in new_translations:
                text.insert("end", msg + '\n')

            text.configure(state='disabled')
            text.yview("end")

            time.sleep(1)
        except:
            time.sleep(1)
            continue
