import tkinter as tk
from tkinter import ttk

from roles import Roles
from widgets.scrollable_text_widget import ScrollableTextWidget
from widgets.send_message_widget import SendMessageWidget
from granmagotchi import font

class ChatView(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.state = state

        self.chat = ScrollableTextWidget(self)
        self.chat.text.tag_configure(Roles.ADMIN, justify="center", foreground="purple")
        self.chat.text.tag_configure(Roles.GRANDMA,justify="left", foreground="green")
        self.chat.text.tag_configure(Roles.USER, justify="right", foreground="blue")
        self.chat.text.configure(font=font)
        self.chat.grid(row=0, column=0, sticky=tk.NSEW)

        self.user_entry = SendMessageWidget(self)
        self.user_input = tk.StringVar()
        self.user_entry.entry.configure(textvariable=self.user_input, font=font)
        self.user_entry.submit.configure(command=self.submit_input)
        self.user_entry.grid(row=1, column=0, sticky=tk.NSEW)

        self.send_message(Roles.ADMIN, "WELCOME TO GRANMAGOTCHI!!!")

    def submit_input(self, *_):
        if self.user_input.get().strip() != "":
            self.state.last_sent_user.set(self.user_input.get().strip())
            self.send_message(Roles.USER, self.state.last_sent_user.get().strip())
            self.user_input.set("")

    def send_message(self, role, message):
        self.chat.text.configure(state=tk.NORMAL)
        if role == Roles.ADMIN:
            self.chat.text.insert(tk.END, f"{message:_^50}\n\n", Roles.ADMIN)

        elif role == Roles.USER:
            try:
                if self.chat.text.tag_names("end-2c")[0] != Roles.USER:
                    self.chat.text.insert(tk.END, "User:\n", Roles.USER)
            except IndexError:
                self.chat.text.insert(tk.END, "User:\n", Roles.USER)

            self.chat.text.insert(tk.END, f"{message}\n", Roles.USER)

        elif role == Roles.GRANDMA:
            try:
                if self.chat.text.tag_names("end-2c")[0] != Roles.GRANDMA:
                    self.chat.text.insert(tk.END, "Grandma:\n", Roles.GRANDMA)
            except IndexError:
                    self.chat.text.insert(tk.END, "Grandma:\n", Roles.GRANDMA)

            self.chat.text.insert(tk.END, f"{message}\n", Roles.GRANDMA)
        self.chat.text.configure(state=tk.DISABLED)