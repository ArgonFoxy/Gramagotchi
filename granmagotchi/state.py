import random
import tkinter as tk

from granmagotchi import grandma_names, grandma_traits

class AppState:
    def __init__(self):
        self.last_sent_user = tk.StringVar()
        self.grandma_age = random.randint(80, 100)
        self.grandma_name = random.choice(grandma_names)
        self.grandma_traits = random.choices(grandma_traits, k=5)
        self.grandma_health = tk.IntVar(value=100)
        self.grandma_satiation = tk.IntVar(value=100)
        self.grandma_hydration = tk.IntVar(value=100)
        self.grandma_happiness = tk.IntVar(value=100)
        self.visible_message_history = []
        self.awaiting_response = False
        self.backstories = []

        self.grey_fog = False
        self.fallback = False