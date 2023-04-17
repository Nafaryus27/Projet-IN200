import random
import tkinter as tk
from tkinter import ttk, filedialog
from .utils import LabeledEntry, LabeledSpinbox


def rgb_to_hex(r,g,b):
    """
    Convertis une couleur rgb en hexadécimal
    """
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def random_color():
    """
    génère une couleur aléatoire au format rgb hexadécimal
    """
    r,g,b, = (random.randint(0,255) for i in range(3))
    return rgb_to_hex(r,g,b)

class StartPageCTRL:
    def __init__(self, master, controller, model_ctrl, simulation_view_ctrl):
        """
        initialisation du controlleur de la page de démarrage
        
        :param master: widget parent de la vue de simulation
        :param controller: controlleur, racine de l'interface
        graphique contenant la Frame courante
        :param model_ctrl: controlleur du model
        :param simulation_view_ctrl: controlleur de la vue de simulation
        """
        
        self.view = StartPage(master, self)
        
        self.controller = controller
        self.model = None
        self.model_ctrl = model_ctrl
        self.simulation_view = simulation_view_ctrl


    def set_model(self, model):
        self.model = model
        
            
    def show(self):
        self.controller.set_top_frame(self)
        self.view.tkraise()

            
    def get_rule(self, first_color):
        r  = self.view.rule_entry.get()
        rule = {}
        v = {"R":1, "L":-1}
        c = random_color()
        color = first_color
        i = 0
        while i < len(r)-1:
            next_color = random_color()
            rule[color] = (v[r[i]], next_color)
            color = next_color
            i += 1
        rule[color] = (v[r[i]], first_color)
        return (rule)

    
    def launch_callback(self):
        x = int(self.view.x_entry.get())
        y = int(self.view.y_entry.get())
        direction = ["Up","Left", "Down", "Right"].index(self.view.direction_entry.get())
        world_size = int(self.view.world_size_entry.get())
        color = self.view.base_color_entry.get()
        rule = self.get_rule(color)

        self.model_ctrl.new_ant(x,y,direction,rule,world_size,color)
        self.simulation_view.launch(world_size, color)
    
        
    def load_file(self):
        file_path = filedialog.askopenfilename(initialdir = "./Saves", title = "Load instance", filetypes = (("Ant File", "*.ant*"), ("all files","*.*")))
        if file_path:
            self.model_ctrl.load(file_path)

    
    def set_model(self, model):
        self.model = model

        
class StartPage(ttk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)

        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid(row=0, column=0, sticky="news")
       
        self.init_widgets()


    def init_widgets(self):
        """
        Initialisation et placement des widgets de la page de démarrage
        """
        self.cont = ttk.Frame(self)
        self.cont.grid(row=1, column=1)

        self.world_size_entry = LabeledSpinbox(self.cont, "World size", 100)
        self.base_color_entry = LabeledEntry(self.cont, "Base color", "White")
        
        self.x_entry = LabeledSpinbox(self.cont, "X start position", 50)
        self.y_entry = LabeledSpinbox(self.cont, "Y start position", 50)
        self.direction_entry = LabeledEntry(self.cont, "Direction", "Up")
        
        self.rule_entry = LabeledEntry(self.cont, text="Rule", default_value="RL")
        self.launch_button = ttk.Button(self.cont, text="Launch", command=self.controller.launch_callback)
        self.load_button = ttk.Button(self.cont, text="Load", command=self.controller.load_file)

        self.world_size_entry.grid(row=0, column=0, sticky='nes')
        self.base_color_entry.grid(row=1, column=0, sticky='nes')
        self.x_entry.grid(row=2,column=0, sticky='nes')
        self.y_entry.grid(row=3,column=0, sticky='nes')
        self.direction_entry.grid(row=4,column=0, sticky='nes')
        self.rule_entry.grid(row=5, column=0, sticky='nes')
        self.launch_button.grid(row=6, column=0, sticky='news')
        self.load_button.grid(row=7, column=0, sticky='news')
