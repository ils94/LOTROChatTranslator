from googletrans import Translator
import pyperclip


def translate_my_message(text, lang):
    try:
        translator = Translator(service_urls=['translate.googleapis.com'])
        x = translator.translate(text.get("1.0", "end"), dest=lang)
        pyperclip.copy(x.text)
        text.delete("1.0", "end")
        text.insert("end", x.text)
    except Exception as e:
        print(e)
