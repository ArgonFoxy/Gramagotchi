import tkinter as tk
from tkinter import ttk

class ScrollableTextWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.rowconfigure(0, weight=1)

        self.text = tk.Text(self)
        self.text.grid(row=0, column=0, sticky=tk.NSEW)

        self.scrollbar = ttk.Scrollbar(self, command=self.text.yview)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.text.configure(yscrollcommand=self.scrollbar.set)