import tkinter as tk
from tkinter import ttk

from .scrollable_text_widget import ScrollableTextWidget
from .send_message_widget import SendMessageWidget


class ChatWidget(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.state = state

        self.chat = ScrollableTextWidget(self)
        self.chat.text.tag_configure("grandma",justify="left", foreground="green")
        self.chat.text.tag_configure("user", justify="right", foreground="blue")
        self.chat.grid(row=0, column=0, sticky=tk.NSEW)

        self.user_entry = SendMessageWidget(self)
        self.user_input = tk.StringVar()
        self.user_entry.entry.configure(textvariable=self.user_input)
        self.user_entry.submit.configure(command=self.submit_input)
        self.user_entry.grid(row=1, column=0, sticky=tk.NSEW)

    def submit_input(self):
        self.state.last_sent_user.set(self.user_input.get())
        self.send_message(True, self.state.last_sent_user.get())
        self.user_input.set("")


    def send_message(self, is_user, message):
        self.chat.text.configure(state=tk.NORMAL)
        if is_user:
            try:
                if self.chat.text.tag_names("insert-1c")[0] != "user":
                    self.chat.text.insert(tk.INSERT, "User:\n", "user")
            except IndexError:
                self.chat.text.insert(tk.INSERT, "User:\n", "user")

            self.chat.text.insert(tk.INSERT, f"{message}\n", "user")
        else:
            try:
                if self.chat.text.tag_names("insert-1c")[0] != "grandma":
                    self.chat.text.insert(tk.INSERT, "Grandma:\n", "grandma")
            except IndexError:
                    self.chat.text.insert(tk.INSERT, "Grandma:\n", "grandma")

            self.chat.text.insert(tk.INSERT, f"{message}\n", "grandma")
        self.chat.text.configure(state=tk.DISABLED)

