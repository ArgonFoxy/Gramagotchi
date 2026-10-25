import tkinter as tk
from threading import Thread
from tkinter import ttk

from roles import Roles
from widgets.scrollable_text_widget import ScrollableTextWidget
from widgets.send_message_widget import SendMessageWidget
from granmagotchi import font

from services import grandma_service

def send_ai_message(ch_view, state ):
    try:
        state.awaiting_response = True
        ch_view.send_message(Roles.GRANDMA, grandma_service.get_ai_response(state))
        grandma_service.increase_stat(state.grandma_happiness, 30)
    except ConnectionError:
        ch_view.send_message(Roles.ADMIN, "Looks like the interactive grandma isn't available right now.\n"
                                          "Check that ollama is running\n"
                                          "Check that the models are installed.")
    finally:
        state.awaiting_response = False

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
        self.user_entry.entry.bind("<Return>", self.submit_input)
        self.user_entry.submit.configure(command=self.submit_input)
        self.user_entry.grid(row=1, column=0, sticky=tk.NSEW)

        self.send_message(Roles.ADMIN, "WELCOME TO GRANMAGOTCHI!!!")

    def submit_input(self, *_):
        if self.user_input.get().strip() != "" and not self.state.awaiting_response:
            self.state.last_sent_user.set(self.user_input.get().strip())
            self.send_message(Roles.USER, self.state.last_sent_user.get().strip())
            self.user_input.set("")

            if self.state.grey_fog:
                match self.state.last_sent_user.get().strip():
                    case "1":
                        self.send_message(Roles.ADMIN, "Set all stats to 0...")
                        self.state.grandma_health.set(0)
                        self.state.grandma_satiation.set(0)
                        self.state.grandma_hydration.set(0)
                        self.state.grandma_happiness.set(0)

                    case "2":
                        self.send_message(Roles.ADMIN, f"Grandma name: {self.state.grandma_name}\n"
                                                       f"Grandma age: {self.state.grandma_age}\n"
                                                       f"Grandma traits: {self.state.grandma_traits}\n"
                                                       f"Grandma health: {self.state.grandma_health.get()}\n"
                                                       f"Grandma satiation: {self.state.grandma_satiation.get()}\n"
                                                       f"Grandma hydration: {self.state.grandma_hydration.get()}\n"
                                                       f"Grandma happiness: {self.state.grandma_happiness.get()}")

                    case "3":
                        self.send_message(Roles.ADMIN, "\n".join([str(i) for i in self.state.visible_message_history]))

                    case "4":
                        self.send_message(Roles.ADMIN, "\n".join([str(i) for i in self.state.backstories]))


                    case "0":
                        self.send_message(Roles.ADMIN, "See you soon...")
                        self.state.grey_fog = False
            elif self.state.last_sent_user.get().lower() not in ["i pray to the fool"]:
                thread = Thread(target=send_ai_message, args=(self, self.state))
                thread.start()
            else:
                self.state.grey_fog = True

                self.send_message(Roles.ADMIN, "Grey fog clouds your vision...")
                self.send_message(Roles.ADMIN, "")
                self.send_message(Roles.ADMIN, "1: Set All Stats To 0")
                self.send_message(Roles.ADMIN, "2: Display minor stats")
                self.send_message(Roles.ADMIN, "3: Show message history")
                self.send_message(Roles.ADMIN, "4: Show grandma backstories")
                self.send_message(Roles.ADMIN, "0: Leave")



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