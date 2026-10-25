import tkinter as tk
from tkinter import ttk

class GrandmaWidget(ttk.Frame):
    def __init__(self, parent, grandma_name_age):
        super().__init__(parent)
        self.configure(height=150, width=150, relief=tk.RAISED)
        self.columnconfigure(0, weight=1, minsize=150)
        self.rowconfigure(0, weight=1, minsize=130)
        self.rowconfigure(1, weight=0)

        self.grandma_name = ttk.Label(self, text=grandma_name_age)
        self.grandma_name.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=4)