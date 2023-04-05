import tkinter as tk
from tkinter import ttk
from .viewer import *
from .utils import ToolBar

class SimulationViewCTRL:
    def __init__(self, master):
        
        self.view = SimulationView(master, self)

    def set_model(self, model):
        self.model = model

    def show(self):
        self.view.tkraise()
        
    def step(self):
        x,y,c = self.model.iterate()
        self.view.set_color(x,y,c)
    
    def previous(self):
        x,y,c = self.model.iterate_previous()
        self.view.set_color(x,y,c)

    def play(self):
        pass

    def pause(self):
        pass

    def reset(self):
        self.model.reset()
        self.view.reset()

    
class SimulationView(ttk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)

        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        tool_bar = ToolBar(self)
        tool_bar.grid(row=0, column=0, sticky='ew')

        self.viewer = Viewer(self, 900, 900, 15, "white")
        self.viewer.grid(row=1, column=1, sticky='news')

        self.grid(row=0, column=0, sticky="news")

    def set_color(self, x:int, y:int, color:str):
        self.viewer.set_color(x,y,color)

    def reset(self):
        self.viewer.reset()
