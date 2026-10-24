import tkinter as tk
from tkinter import ttk

from state import AppState
from views.gotchi_view import GotchiView
from views.chat_view import ChatView

class Granmagotchi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.state = AppState()

        self.gotchi_view = GotchiView(self, self.state)
        self.gotchi_view.grid(row=0, column=0, sticky=tk.NSEW)

        self.chat_view = ChatView(self, self.state)
        self.chat_view.grid(row=0,column=1,sticky=tk.NSEW)

        self.style = ttk.Style()
        # self.tk.call('source', './assets/themes/aquativo.tcl')
        # self.tk.call('source', './assets/themes/aquativoImageLib.tcl')
        # self.style.theme_use("aquativo")

        self.tk.call('source', './assets/themes/winxpblue.tcl')
        self.tk.call('source', './assets/themes/winxpblueImageLib.tcl')
        self.style.theme_use("winxpblue")


        self.style.configure('.', font=("8514oem", "12"))
