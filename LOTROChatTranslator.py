import tkinter as tk
from tkinter import tix
import create_window
import center_windows
import os


def create_tooltip(widget, text):
    balloon = tix.Balloon(widget, initwait=500)
    balloon.bind_widget(widget, balloonmsg=text)


def button_click(button_name):
    create_window.create_window(button_name)


root = tix.Tk()
root.geometry("250x50")
root.resizable(False, False)
root.title("Chat Type")

if os.path.isfile('icon.ico'):
    root.iconbitmap('icon.ico')

center_windows.center_window(root, 250, 50)

button_texts = ["Common Chat", "IMs Chat"]
tooltips = ["Use this for World, Fellowship, Kinship and etc.", "Use this only for IMs Chats (due different Timestamp)"]

for i, (text, tooltip_text) in enumerate(zip(button_texts, tooltips)):
    button = tk.Button(root, text=text, width=15, command=lambda t=text: button_click(t))
    button.grid(row=0, column=i, padx=5, pady=10)
    create_tooltip(button, tooltip_text)

root.mainloop()
