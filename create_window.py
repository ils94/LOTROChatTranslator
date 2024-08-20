import tkinter as tk
from tkinter import tix
from tkinter import ttk, filedialog
import quick_translator
import json
import os
import supported_languages
import translate_chat
import threading
import center_windows

lotro_folder = os.path.join(os.path.expanduser("~"), "Documents", "The Lord of the Rings Online")


def create_window(window_name):
    language_names = {v: k for k, v in supported_languages.languages.items()}

    settings_file = "selected_languages.json"
    stop_event = threading.Event()
    translation_thread = None

    def create_tooltip(widget, text):
        balloon = tix.Balloon(widget, initwait=100)
        balloon.bind_widget(widget, balloonmsg=text)

    def save_settings():
        settings = {
            "chat_language": chat_var.get(),
            "translator_language": translator_var.get(),
        }
        with open(settings_file, 'w') as f:
            json.dump(settings, f)

    def load_settings():
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings = json.load(f)
                chat_var.set(settings.get("chat_language", list(language_names.keys())[0]))
                translator_var.set(settings.get("translator_language", list(language_names.keys())[0]))

    def on_enter(event):
        selected_language = language_names[translator_var.get()]

        x = threading.Thread(target=quick_translator.translate_my_message, args=(text2, selected_language))
        x.setDaemon(True)
        x.start()

        return "break"

    def open_file():
        file_path = filedialog.askopenfilename(initialdir=lotro_folder, filetypes=[("Text Files", "*.txt")])

        if file_path:
            file_entry.delete(0, tk.END)
            file_entry.insert(0, file_path)

    def clear_chat():
        text1.configure(state='normal')
        text1.delete(1.0, tk.END)
        text1.configure(state='disabled')

    def save_chat_settings():
        nonlocal translation_thread

        clear_chat()

        if translation_thread and translation_thread.is_alive():
            stop_event.set()
            translation_thread.join()

        stop_event.clear()

        selected_language = language_names[chat_var.get()]
        translation_thread = threading.Thread(target=translate_chat.translate, args=(
            window_name, text1, file_entry.get(), selected_language, stop_event))
        translation_thread.setDaemon(True)
        translation_thread.start()

    def on_closing():
        stop_event.set()
        if translation_thread and translation_thread.is_alive():
            translation_thread.join()
        toplevel.destroy()

    toplevel = tk.Toplevel()
    toplevel.geometry("500x500")
    toplevel.attributes("-topmost", True)
    toplevel.title(f"LOTRO Chat Translator: {window_name}")

    menu_bar = tk.Menu(toplevel)
    toplevel.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Clear Chat", command=clear_chat)
    file_menu.add_command(label="Save Settings", command=save_chat_settings)

    center_windows.center_window(toplevel, 500, 500)

    toplevel.grid_rowconfigure(0, weight=0)
    toplevel.grid_rowconfigure(1, weight=0)
    toplevel.grid_rowconfigure(2, weight=1)
    toplevel.grid_columnconfigure(0, weight=1)

    entry_frame = tk.Frame(toplevel)
    entry_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    create_tooltip(entry_frame,
                   "The path to your chat log file.txt. You can paste the full path in the text box, or use the Browse button to open it.")

    path_label = tk.Label(entry_frame, text="Path to the log file")
    path_label.grid(row=0, column=0, padx=(0, 5), pady=5, sticky="w")

    file_entry = tk.Entry(entry_frame)
    file_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="ew")

    file_button = tk.Button(entry_frame, text="Browse", width=10, command=open_file)
    file_button.grid(row=0, column=2, padx=(0, 5), sticky="ew")

    combobox_frame = tk.Frame(toplevel)
    combobox_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    chat_label = tk.Label(combobox_frame, text="Chat")
    chat_label.grid(row=0, column=0, padx=(0, 5))

    chat_var = tk.StringVar()
    chat_combobox = ttk.Combobox(combobox_frame, textvariable=chat_var, values=list(language_names.keys()),
                                 state="readonly")
    chat_combobox.grid(row=0, column=1, padx=(0, 5), sticky="ew")
    create_tooltip(chat_combobox, "The language you want to translate the Chat.")

    translator_label = tk.Label(combobox_frame, text="Translator")
    translator_label.grid(row=0, column=2, padx=(0, 5))

    translator_var = tk.StringVar()
    translator_combobox = ttk.Combobox(combobox_frame, textvariable=translator_var, values=list(language_names.keys()),
                                       state="readonly")
    translator_combobox.grid(row=0, column=3, sticky="ew")
    create_tooltip(translator_combobox, "The language you want to translate what you type in the Translator.")

    text_frame = tk.Frame(toplevel)
    text_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    chat_text_label = tk.Label(text_frame, text="Chat")
    chat_text_label.grid(row=0, column=0, sticky="w")

    text1 = tk.Text(text_frame, height=10)
    text1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    text1.configure(state='disabled')
    create_tooltip(text1, "Your translated chat will appear here.")

    translator_text_label = tk.Label(text_frame, text="Translator")
    translator_text_label.grid(row=2, column=0, sticky="w")

    text2 = tk.Text(text_frame, height=5)
    text2.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    create_tooltip(text2,
                   "Type something here, and press ENTER. The typed text will be changed to it's translated version. You can then just paste it (Ctrl + V) on LOTRO chat!")

    text2.bind("<Return>", on_enter)

    load_settings()

    chat_combobox.bind("<<ComboboxSelected>>", lambda e: save_settings())
    translator_combobox.bind("<<ComboboxSelected>>", lambda e: save_settings())

    entry_frame.grid_columnconfigure(0, weight=0)
    entry_frame.grid_columnconfigure(1, weight=1)
    entry_frame.grid_columnconfigure(2, weight=0)
    combobox_frame.grid_columnconfigure(0, weight=0)
    combobox_frame.grid_columnconfigure(1, weight=1)
    combobox_frame.grid_columnconfigure(2, weight=0)
    combobox_frame.grid_columnconfigure(3, weight=1)
    text_frame.grid_rowconfigure(1, weight=1)
    text_frame.grid_rowconfigure(3, weight=0)
    text_frame.grid_columnconfigure(0, weight=1)

    toplevel.protocol("WM_DELETE_WINDOW", on_closing)
