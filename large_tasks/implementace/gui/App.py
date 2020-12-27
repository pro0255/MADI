from tkinter import *
from tkinter.ttk import Progressbar
from gui.GUI_CONSTANTS import GLOBAL_HEIGHT, GLOBAL_WIDTH, INIT_DATASET, GLOBAL_OPTION_MENU_COLOR
from gui.datasets import datasets
from utils.k_means import k_means
from vizualization.draw2d import draw2d
from utils.sse import total_sse
from gui.Console import ConsoleUi
import matplotlib.pyplot as plt



class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        self.checkbuttons = []
        self.picks = picks
        self.parent = parent
        self.side = side
        self.anchor = anchor
        self.draw()

    def draw(self):
        for c in self.checkbuttons:
            c.pack_forget()
        self.checkbuttons = []
        self.vars = [] 
        for pick in self.picks:
            var = IntVar(self.parent)
            chk = Checkbutton(self, text=pick, variable=var, command=self.disable_rest)
            chk.pack(side=self.side, anchor=self.anchor, expand=YES)
            self.checkbuttons.append(chk)
            self.vars.append(var)

    def disable_rest(self):
        try:
            index = list(self.state()).index(1)
            for i, c in enumerate(self.checkbuttons):
                if i != index:
                    c.config(state="disabled")
        except:
            for c in self.checkbuttons:
                c.config(state="active")

    def state(self):
        return map((lambda var: var.get()), self.vars)


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
        self.create_progressbar()
        self.create_combo_box()
        self.create_slider()
        self.create_number_of_kmeans_slider()
        self.create_console()
        self.create_run_button()

        self.create_checkbox_visualization()
        self.create_feature_checkbar()
        self.create_visualization_button()
        self.checkbox_action()

    def create_console(self):
        self.console = ConsoleUi(self.root)

    def create_slider(self):
        self.kSlider = Scale(self.root, from_=2, to=50, orient="horizontal", label="Number of clusters [k]")
        self.kSlider.pack()

    def create_number_of_kmeans_slider(self):
        self.kMeansSlider = Scale(self.root, from_=1, to=50, orient="horizontal", label="Number k means")
        self.kMeansSlider.pack()

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

    def create_checkbox_visualization(self):
        self.show_visualization = IntVar(self.root)
        self.show_visualization.set(0)
        self.checkbox = Checkbutton(self.root, text="Show visualization", variable=self.show_visualization, command=self.checkbox_action)
        self.checkbox.pack()

    def create_feature_checkbar(self):
        features = self.selected_dS.get_preprocessed_features()
        self.x = Checkbar(self.root, features)
        self.y = Checkbar(self.root, features)
        self.x.pack()
        self.y.pack()

    def create_progressbar(self):
        self.progress_bar = Progressbar(self.root, orient = HORIZONTAL, 
              length = GLOBAL_WIDTH, mode = 'determinate')
        self.progress_bar.pack() 

    def checkbox_action(self):
        if hasattr(self, 'x') and hasattr(self, 'y') and hasattr(self, 'show_visualization') and hasattr(self, 'vis_button'): 
            if self.show_visualization.get() == 1:
                self.x.pack()
                self.y.pack()
                self.vis_button.pack()
            else:
                self.x.pack_forget()
                self.y.pack_forget()
                self.vis_button.pack_forget()

    def create_visualization_button(self):
        self.vis_button = Button(
            self.root,
            text="make visualization",
            bg="brown",
            fg="white",
            font=("helvetica", 9, "bold"),
            command=self.run_visualization,
            width=GLOBAL_WIDTH,
        )
        self.vis_button.config(state="disabled")
        self.vis_button.pack() 

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
        if hasattr(self, 'x') and hasattr(self, 'y'):
            features = self.selected_dS.get_preprocessed_features()
            self.x.picks = features
            self.y.picks = features
            self.x.draw()
            self.y.draw()


    def run_action(self):
        k = self.kSlider.get()
        self.selected_dS.load()
        dS = self.selected_dS.preprocess()

        number_of_times = self.kMeansSlider.get()

        self.console.display(f'Starting processing')

        best = None
        for i in range(number_of_times):
            
            #TODO!: make thread
            progress_value = 100* ((i+1)/number_of_times)
            self.progress_bar['value'] = progress_value


            result = k_means(dS, k)
            current_sse = total_sse(result[2])
            self.console.display(f'Iteration {i} -> {current_sse}')
            if best is None:
                best = (current_sse, result)
            else:
                if current_sse < best[0]:
                    best = (current_sse, result)
        self.console.display(f'\nFinished.. lowest sse is {best[0]}\n')

        self.vis_button.config(state="active")
        self.best = best

    def run_visualization(self):
        if self.show_visualization.get() and hasattr(self, 'best'):
            try:
                xIndex = list(self.x.state()).index(1)
                yIndex = list(self.y.state()).index(1)

                if xIndex == yIndex:
                    raise Exception('Cannot be same attributes')

                features = self.selected_dS.get_preprocessed_features()
                xLabel = features[xIndex]
                yLabel = features[yIndex]
                draw2d(*self.best[1], (xIndex, yIndex), (xLabel, yLabel))
                plt.show()
            except Exception as e:
                print('Something went wrong with visualization')
                print(e)




    def start(self, force=True):
        """Starts GUI"""
        if force:
            self.run_action()
        else:
            self.root.mainloop()

    def stop(self):
        """Stops GUI"""
        self.root.destroy()

