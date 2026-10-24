import tkinter as tk
from tkinter import ttk

from granmagotchi import font

class SendMessageWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.rowconfigure(0, weight=1)

        self.entry = ttk.Entry(self, font=font)
        self.entry.grid(row=0, column=0, sticky=tk.EW)

        self.submit = ttk.Button(self, text=">", width=3)
        self.submit.grid(row=0, column=1)

    def assign_command(self, command):
        self.submit.configure(command=command)