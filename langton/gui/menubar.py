import tkinter as tk
from tkinter import ttk

class MenuBarCTRL:
    def __init__(self, master, start_page_ctrl, simulation_ctrl):

        self.view = MenuBar(master, self)
        self.simulation = simulation_ctrl
        self.start_page = start_page_ctrl

    def set_model(self, model):
        self.model = model
        
    def new_sim(self):
        self.simulation.reset()
        self.start_page.show()
        

    def load_file(self):
        pass

    def save_file(self):
        pass

    def settings(self):
        pass

    def step(self):
        self.simulation.step()

    def previous(self):
        self.simulation.previous()

    def play(self):
        self.simulation.play()

    def pause(self):
        self.simulation.pause()

    def reset(self):
        self.simulation.reset()

    def documentation(self):
        pass

    def about(self):
        pass

    
class MenuBar(tk.Menu):
    def __init__(self, master, controller):
        tk.Menu.__init__(self, master)

        self.controller = controller
        self.init_widgets()
        master['menu'] = self
        
    def init_widgets(self):
        menu_file = tk.Menu(self)
        menu_file.add_command(label="New", command=self.controller.new_sim)
        menu_file.add_command(label="Load", command=self.controller.load_file)
        menu_file.add_command(label="Save", command=self.controller.save_file)
        menu_file.add_separator()
        menu_file.add_command(label="Settings", command=self.controller.settings)
        menu_file.add_command(label="Quit", command=self.master.destroy)

        self.add_cascade(menu=menu_file, label="File")

        menu_sim = tk.Menu(self)
        menu_sim.add_command(label="Next", command=self.controller.step)
        menu_sim.add_command(label="Previous", command=self.controller.previous)
        menu_sim.add_separator()
        menu_sim.add_command(label="Play", command=self.controller.play)
        menu_sim.add_command(label="Pause", command=self.controller.pause)
        menu_sim.add_separator()
        menu_sim.add_command(label="Reset", command=self.controller.reset)

        self.add_cascade(menu=menu_sim, label="Simulation")

        menu_help = tk.Menu(self)
        menu_help.add_command(label="Documentation", command=self.controller.documentation)
        menu_help.add_command(label="About", command=self.controller.about)
        self.add_cascade(menu=menu_help, label="Help")
