import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from widgets.bar_widget import BarWidget
from widgets.grandma_widget import GrandmaWidget
from widgets.four_button_widget import FourButtonWidget

from services import grandma_service

class GotchiView(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1, minsize=150)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.state=state

        self.grandma_widget = GrandmaWidget(self, f"{self.state.grandma_name}, {self.state.grandma_age}")
        self.grandma_widget.grid(row=0, column=0, padx=10)

        self.stat_container = ttk.Frame(self)
        self.stat_container.grid(row=1, column=0, sticky=tk.NSEW)

        self.stat_container.columnconfigure(0, weight=1)

        self.stat_container.rowconfigure(0)
        self.stat_container.rowconfigure(1)
        self.stat_container.rowconfigure(2)
        self.stat_container.rowconfigure(3)

        self.health_stat = BarWidget(self.stat_container, "Health", state.grandma_health)
        self.health_stat.grid(row=0, column=0, sticky=tk.EW, padx=25)

        self.satiation_stat = BarWidget(self.stat_container, "Satiation", state.grandma_satiation)
        self.satiation_stat.grid(row=1, column=0, sticky=tk.EW, padx=25)

        self.hydration_stat = BarWidget(self.stat_container, "Hydration", state.grandma_hydration)
        self.hydration_stat.grid(row=2, column=0, sticky=tk.EW, padx=25)

        self.happiness_stat = BarWidget(self.stat_container, "Happiness", state.grandma_happiness)
        self.happiness_stat.grid(row=3, column=0, sticky=tk.EW, padx=25)


        self.button_group = FourButtonWidget(self)
        self.button_group.grid(row=2, column=0, sticky=tk.NSEW)

        self.pills_icon = ImageTk.PhotoImage(Image.open("./assets/images/pills.png").resize((25,20)))
        self.button_group.button_top_left.configure(command=self.meds, image=self.pills_icon, compound="center")

        self.soup_icon = ImageTk.PhotoImage(Image.open("./assets/images/soup.png").resize((25, 20)))
        self.button_group.button_top_right.configure(command=self.food, image=self.soup_icon, compound="center")

        self.water_icon = ImageTk.PhotoImage(Image.open("./assets/images/water.png").resize((25, 20)))
        self.button_group.button_bottom_left.configure(command=self.water, image=self.water_icon, compound="center")

        self.shower_icon = ImageTk.PhotoImage(Image.open("./assets/images/shower.png").resize((25, 20)))
        self.button_group.button_bottom_right.configure(image=self.shower_icon, compound="center")

    def meds(self):
        if not grandma_service.increase_stat(self.state.grandma_health, 30):
            self.event_generate("<<AlreadyHealthy>>")

    def food(self):
        if not grandma_service.increase_stat(self.state.grandma_satiation, 30):
            self.event_generate("<<AlreadySated>>")

    def water(self):
        if not grandma_service.increase_stat(self.state.grandma_hydration, 30):
            self.event_generate("<<AlreadyHydrated>>")