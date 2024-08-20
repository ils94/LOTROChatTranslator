from googletrans import Translator
import pyperclip


def translate_my_message(text1, text2, lang):
    try:
        translator = Translator(service_urls=['translate.googleapis.com'])
        x = translator.translate(text1.get("1.0", "end"), dest=lang)
        pyperclip.copy(x.text)
        text2.delete("1.0", "end")
        text2.insert("end", x.text)
    except Exception as e:
        print(e)
