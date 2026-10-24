import tkinter as tk
from random import choice
from granmagotchi import grandma_names

class AppState:
    def __init__(self):
        self.last_sent_user = tk.StringVar()
        self.grandma_name = tk.StringVar(value=choice(grandma_names))
        self.grandma_hunger = tk.IntVar(value=100)
        self.grandma_health = tk.IntVar(value=100)