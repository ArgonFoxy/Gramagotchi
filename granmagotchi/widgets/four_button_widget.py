import tkinter as tk
from tkinter import ttk

class FourButtonWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.button_top_left = ttk.Button(self, width=3)
        self.button_top_left.grid(row=0, column=0, ipadx=10, ipady=10, sticky=tk.N)

        self.button_top_right = ttk.Button(self, width=3)
        self.button_top_right.grid(row=0, column=1, ipadx=10, ipady=10, sticky=tk.N)

        self.button_bottom_left = ttk.Button(self, width=3)
        self.button_bottom_left.grid(row=1, column=0, ipadx=10, ipady=10, sticky=tk.N)

        self.button_bottom_right = ttk.Button(self, width=3)
        self.button_bottom_right.grid(row=1, column=1, ipadx=10, ipady=10, sticky=tk.N)