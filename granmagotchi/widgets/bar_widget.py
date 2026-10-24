import tkinter as tk
from tkinter import ttk

class BarWidget(ttk.Frame):
    def __init__(self, parent, name, value):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.label = ttk.Label(self, text=name)
        self.label.grid(row=0,column=0,sticky=tk.S + tk.EW)

        self.bar = ttk.Progressbar(self, maximum=100, variable=value)
        self.bar.grid(row=1,column=0,sticky=tk.EW + tk.N)