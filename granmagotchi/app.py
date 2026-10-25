import random
import tkinter as tk
from tkinter import ttk
from threading import Thread
from pygame import mixer

from .roles import Roles
from .state import AppState
from .views.gotchi_view import GotchiView
from .views.chat_view import ChatView

from .services import grandma_service

mixer.init()

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

        grandma_service.tick_stat(self, self.state.grandma_health, 10, 40000)
        grandma_service.tick_stat(self, self.state.grandma_satiation, 10, 32000)
        grandma_service.tick_stat(self, self.state.grandma_hydration, 10, 25000)
        grandma_service.tick_stat(self, self.state.grandma_happiness, 10, 20000)

        self.thread = Thread(target=grandma_service.generate_history, args=(0, self.state))
        self.thread.start()

        self.bind("<<AlreadyHealthy>>", self.grandma_healthy)
        self.bind("<<AlreadySated>>", self.grandma_sated)
        self.bind("<<AlreadyHydrated>>", self.grandma_hydrated)

        mixer.music.load("assets/music/bgm.mpeg")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)
        mixer.music.pause()

    def grandma_healthy(self, e):
        self.chat_view.send_message(Roles.GRANDMA, random.choice(
            [
                "Hey, I'm very healthy sweetie!",
                "There is no need for that sweetie.",
                "I am too healthy for that.",
                "You shouldn't concern yourself.",
                "Don't worry about me.",
                "I'm in tip-top shape!"
            ]))

    def grandma_sated(self, e):
        self.chat_view.send_message(Roles.GRANDMA, random.choice(
            [
                "Hey, I'm very full sweetie!",
                "There is no need for that sweetie.",
                "I am too full for that.",
                "You shouldn't concern yourself.",
                "Don't worry about me.",
                "I'm in tip-top shape!"
            ]))

    def grandma_hydrated(self, e):
        self.chat_view.send_message(Roles.GRANDMA, random.choice(
            [
                "Hey, I'm very hydrated sweetie!",
                "There is no need for that sweetie.",
                "I drank too much water already.",
                "You shouldn't concern yourself.",
                "Don't worry about me.",
                "I'm in tip-top shape!"
            ]))