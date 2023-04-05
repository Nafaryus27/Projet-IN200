import tkinter as tk
from tkinter import ttk
from .utils import LabeledEntry

class StartPageCTRL:
    def __init__(self, master, model, simulation_ctrl):
        self.view = StartPage(master, self)
        self.model = model

        self.simulation = simulation_ctrl

    def show(self):
        self.view.tkraise()
        
    def launch_callback(self):
        self.simulation.show()

    def get_rule(self):
        return self.view.rule_entry.get_rule()

    def load_file(Self):
        pass

        
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
        self.cont = ttk.Frame(self)
        self.cont.grid(row=1, column=1)

        self.rule_entry = LabeledEntry(self.cont, "Rule", "RL")
        
        
        self.launch_button = ttk.Button(self.cont, text="Launch", command=self.controller.launch_callback)
        self.load_button = ttk.Button(self.cont, text="Load", command=self.controller.load_file)

        self.rule_entry.grid(row=0, column=0, sticky='news')
        self.launch_button.grid(row=3, column=0, sticky='news')
        self.load_button.grid(row=4, column=0, sticky='news')
