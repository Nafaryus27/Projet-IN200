import tkinter as tk
from tkinter import ttk
from .viewer import *
from .utils import ToolBar

class SimulationViewCTRL:
    def __init__(self, master, model):
        
        self.view = SimulationView(master, self)
        self.model = model

    def show(self):
        self.view.tkraise()
        
    def step(self):
        pass

    def previous(self):
        pass

    def play(self):
        pass

    def pause(self):
        pass

    def reset(self):
        pass

    
class SimulationView(ttk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)

        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        tool_bar = ToolBar(self)
        tool_bar.grid(row=0, column=0, sticky='ew')

        self.viewer = Viewer(self, 900, 900, 15)
        self.viewer.grid(row=1, column=1, sticky='news')

        self.grid(row=0, column=0, sticky="news")
