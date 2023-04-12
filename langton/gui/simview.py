import tkinter as tk
from tkinter import ttk
from .viewer import *
from .utils import ToolBar

class SimulationViewCTRL:
    def __init__(self, master, root):
        self.root = root
        self.view = SimulationView(master, self)

        self.iteration = 0
        self.is_looping = False
        self.speed = 1

        
    def set_model(self, model):
        self.model = model

        
    def show(self, viewer_size, grid_size, default_color):
        self.is_looping = False
        self.model.reset()
        self.view.init_viewer(viewer_size, grid_size, default_color)
        self.view.tkraise()

        
    def step(self):
        x,y,c = self.model.iterate()
        self.view.set_color(x,y,c)

        self.iteration += 1
        self.view.set_iteration(self.iteration)
        return True

    
    def previous(self):
        if self.iteration > 0:
            x,y,c = self.model.iterate_previous()
            self.view.set_color(x,y,c)
            self.iteration -= 1
            self.view.set_iteration(self.iteration)
            return True
        return False

    
    def loop(self):
        if self.is_looping and self.looped_func():
            self.root.after(self.speed, self.loop)
        else:
            self.is_looping = False
            
        
    def play_forward(self):
        self.looped_func = self.step
        if not self.is_looping:
            self.is_looping = True
            self.loop()
        
        
    def play_reverse(self):
        self.looped_func = self.previous
        if not self.is_looping and self.iteration:
            self.is_looping = True
            self.loop()

        
    def pause(self):
        self.is_looping = False

        
    def reset(self):
        self.is_looping = False
        self.iteration = 0
        self.model.reset()
        self.view.reset()

        
    def set_speed(self, s):
        self.speed = s

    
class SimulationView(ttk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)

        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.tool_bar = ToolBar(self, controller)
        self.tool_bar.grid(row=0, column=1, sticky='ew')
        
        self.grid(row=0, column=0, sticky="news")

    def init_viewer(self, pixel_size:int, grid_size:int, default_color):
        self.viewer = Viewer(self, pixel_size, pixel_size, grid_size, default_color)
        self.viewer.grid(row=1, column=1, sticky='ns')

    
    def set_color(self, x:int, y:int, color:str):
        self.viewer.set_color(x,y,color)

    def reset(self):
        self.viewer.reset()

    def set_iteration(self, val):
        self.tool_bar.set_iteration(val)
