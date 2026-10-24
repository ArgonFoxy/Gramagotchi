import tkinter as tk
from tkinter import ttk

class GrandmaWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(height=200, width=200, relief=tk.RAISED)