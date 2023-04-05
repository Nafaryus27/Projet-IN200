import random
import tkinter as tk
from tkinter import ttk
from .utils import LabeledEntryStr, LabeledEntryInt


def rgb_to_hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def random_color():
    r,g,b, = (random.randint(0,255) for i in range(3))
    return rgb_to_hex(r,g,b)

class StartPageCTRL:
    def __init__(self, master, ant_ctrl, simulation_ctrl):
        self.view = StartPage(master, self)

        self.ant_ctrl = ant_ctrl
        self.simulation = simulation_ctrl

    def show(self):
        self.view.tkraise()
        
    def launch_callback(self):
        x,y,direction,world_size,color = self.get_infos()
        rule = self.get_rule(color)
        self.ant_ctrl.new_ant(x,y,direction,rule,world_size,color)
        self.simulation.show()

    def get_rule(self, first_color):
        r  = self.view.rule_entry.get()
        rule = {}
        v = {"R":1, "L":-1}
        c = random_color()
        color = first_color
        i = 0
        while i < len(r)-1:
            next_color = random_color
            rule[color] = (v[r[i]], next_color)
            color = next_color
        rule[color] = (v[r[i]], first_color)
        return (rule)

    def get_info(self):
        x = self.view.x_entry.get()
        y = self.view.y_entry.get()
        direction = self.view.direction_entry.get()
        world_size = self.world_size_entry.get()
        color = self.base_color_entry.get()
        return (x, y, direction, world_size, color)

    def load_file(Self):
        pass

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
        self.cont = ttk.Frame(self)
        self.cont.grid(row=1, column=1)

        self.world_size_entry = LabeledEntryStr(self.cont, "World size", 100)
        self.base_color = LabeledEntryStr(self.cont, "Base color", "White")
        
        self.x_entry = LabeledEntryInt(self.cont, "X start position", 50)
        self.y_entry = LabeledEntryInt(self.cont, "Y start position", 50)
        self.direction_entry = LabeledEntryStr(self.cont, "Direction", "Up")
        
        self.rule_entry = LabeledEntryStr(self.cont, text="Rule", default_value="RL")
        
        self.launch_button = ttk.Button(self.cont, text="Launch", command=self.controller.launch_callback)
        self.load_button = ttk.Button(self.cont, text="Load", command=self.controller.load_file)

        self.world_size_entry.grid(row=0, column=0, sticky='news')
        self.base_color.grid(row=1, column=0, sticky='news')
        self.x_entry.grid(row=2,column=0, sticky='news')
        self.y_entry.grid(row=3,column=0, sticky='news')
        self.direction_entry.grid(row=4,column=0, sticky='news')
        self.rule_entry.grid(row=5, column=0, sticky='news')
        self.launch_button.grid(row=6, column=0, sticky='news')
        self.load_button.grid(row=7, column=0, sticky='news')
