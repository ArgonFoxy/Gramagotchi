import tkinter as tk
from tkinter import ttk

from roles import Roles
from state import AppState
from views.gotchi_view import GotchiView
from views.chat_view import ChatView

from services import grandma_service

class Granmagotchi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("Gramagotchi!")
        self.wm_geometry("1000x500")
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.state = AppState()

        self.gotchi_view = GotchiView(self, self.state)
        self.gotchi_view.grid(row=0, column=0, sticky=tk.NSEW)

        self.chat_view = ChatView(self, self.state)
        self.chat_view.grid(row=0,column=1,sticky=tk.NSEW)

        self.style = ttk.Style()
        self.tk.call('source', './assets/themes/winxpblue.tcl')
        self.tk.call('source', './assets/themes/winxpblueImageLib.tcl')
        self.style.theme_use("winxpblue")
        self.style.configure('.', font=("8514oem", "12"))
        self.style.configure("TButton", anchor="center")

        grandma_service.tick_stat(self, self.state.grandma_health, 10, 23000)
        grandma_service.tick_stat(self, self.state.grandma_satiation, 10, 18000)
        grandma_service.tick_stat(self, self.state.grandma_hydration, 10, 10000)
        grandma_service.tick_stat(self, self.state.grandma_cleanliness, 10, 40000)

        self.bind("<<AlreadyHealthy>>", self.grandma_healthy)
        self.bind("<<AlreadySated>>", self.grandma_sated)
        self.bind("<<AlreadyHydrated>>", self.grandma_hydrated)
        self.bind("<<AlreadyClean>>", self.grandma_clean)

        print(self.state.grandma_traits)

    def grandma_healthy(self, e):
        self.chat_view.send_message(Roles.GRANDMA, "Hey! I'm very healthy sweetie!")

    def grandma_sated(self, e):
        self.chat_view.send_message(Roles.GRANDMA,"Hey! I'm stuffed sweetie!")

    def grandma_hydrated(self, e):
        self.chat_view.send_message(Roles.GRANDMA, "Hey! I'm not thirsty sweetie!")

    def grandma_clean(self, e):
        self.chat_view.send_message(Roles.GRANDMA, "Hey! I'm clean sweetie!")