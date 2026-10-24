import tkinter as tk
from tkinter import ttk

from widgets.bar_widget import BarWidget
from widgets.grandma_widget import GrandmaWidget
from widgets.four_button_widget import FourButtonWidget

class GotchiView(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)


        self.grandma_widget = GrandmaWidget(self)
        self.grandma_widget.grid(row=0, column=0, padx=10)


        self.stat_container = ttk.Frame(self)
        self.stat_container.grid(row=1, column=0, sticky=tk.NSEW)

        self.stat_container.columnconfigure(0, weight=1)

        self.stat_container.rowconfigure(0)
        self.stat_container.rowconfigure(1)
        self.stat_container.rowconfigure(2)

        self.health_stat = BarWidget(self.stat_container, "Health", state.grandma_health)
        self.health_stat.grid(row=0, column=0, sticky=tk.EW, padx=25)

        self.health_stat = BarWidget(self.stat_container, "Hunger", state.grandma_health)
        self.health_stat.grid(row=1, column=0, sticky=tk.EW, padx=25)

        self.health_stat = BarWidget(self.stat_container, "Thirst", state.grandma_health)
        self.health_stat.grid(row=2, column=0, sticky=tk.EW, padx=25)


        self.button_group = FourButtonWidget(self)
        self.button_group.grid(row=2, column=0, sticky=tk.NSEW + tk.N, padx=40)