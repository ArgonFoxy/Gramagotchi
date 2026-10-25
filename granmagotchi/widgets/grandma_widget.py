import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class GrandmaWidget(ttk.Frame):
    def __init__(self, parent, grandma_name_age):
        super().__init__(parent)
        self.configure(height=150, width=150, relief=tk.RAISED)
        self.columnconfigure(0, weight=1, minsize=150)

        self.rowconfigure(0, minsize=30)
        self.rowconfigure(1, weight=1, minsize=100)
        self.rowconfigure(2, weight=0)

        self.grandma_happy = ImageTk.PhotoImage(Image.open("assets/images/grandma_happy.png").resize((100, 100),
                                                                                                     Image.Resampling.NEAREST))
        self.grandma_ok = ImageTk.PhotoImage(Image.open("assets/images/grandma_ok.png").resize((100, 100),
                                                                                                     Image.Resampling.NEAREST))
        self.grandma_sad = ImageTk.PhotoImage(Image.open("assets/images/grandma_sad.png").resize((100, 100),
                                                                                                     Image.Resampling.NEAREST))
        self.grandma_view = ttk.Label(self, image=self.grandma_happy, anchor="center")
        self.grandma_view.grid(row=1, column=0, sticky=tk.NS, padx=5, pady=2)

        self.grandma_name = ttk.Label(self, text=grandma_name_age)
        self.grandma_name.grid(row=2, column=0, sticky=tk.EW, padx=5, pady=2)

    def set_mood(self, value):
        if value < 30:
            self.grandma_view.configure(image=self.grandma_sad)
        elif value < 60:
            self.grandma_view.configure(image=self.grandma_ok)
        else:
            self.grandma_view.configure(image=self.grandma_happy)