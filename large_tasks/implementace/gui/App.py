from tkinter import *
from gui.GUI_CONSTANTS import GLOBAL_HEIGHT, GLOBAL_WIDTH, INIT_DATASET, GLOBAL_OPTION_MENU_COLOR
from gui.datasets import datasets
from utils.k_means import k_means
from vizualization.draw2d import draw2d

class Application:

    def __init__(self):
        self.init_set()
        self.init_create()

    def init_set(self):
        self.root = Tk()
        self.root.title("MAD")
        self.root.geometry(f"{GLOBAL_WIDTH}x{GLOBAL_HEIGHT}")
        self.selected_dS = datasets[INIT_DATASET]

    def init_create(self):
        self.create_combo_box()
        self.create_run_button()

    def create_combo_box(self):
        choices = list(datasets.keys())
        variable = StringVar(self.root)
        init_dS = INIT_DATASET
        variable.set(init_dS)
        self.select_dS_action(init_dS)
        menu = OptionMenu(
            self.root, variable, *choices, command=self.select_dS_action
        )
        menu.configure(width=GLOBAL_WIDTH, bg=GLOBAL_OPTION_MENU_COLOR)
        menu.pack()

    def create_run_button(self):
        self.run_button = Button(
            self.root,
            text="start",
            bg="brown",
            fg="white",
            font=("helvetica", 9, "bold"),
            command=self.run_action,
            width=GLOBAL_WIDTH,
        )
        self.run_button.pack()


    def select_dS_action(self, value):
        self.selected_dS = datasets[value]

    def run_action(self):
        k = 3
        self.selected_dS.load()
        dS = self.selected_dS.preprocess()
        result = k_means(dS, k)
        draw2d(*result, (0, 1))    

    def start(self, force=True):
        """Starts GUI"""
        if force:
            self.run_action()
        else:
            self.root.mainloop()

    def stop(self):
        """Stops GUI"""
        self.root.destroy()

