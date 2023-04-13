import tkinter as tk
from tkinter import ttk, filedialog

class MenuBarCTRL:
    def __init__(self, master, ant_ctrl, start_page_ctrl, simulation_ctrl):
        self.view = MenuBar(master, self)
        self.disable_sim()
        self.disable_save()
        self.simulation = simulation_ctrl
        self.start_page = start_page_ctrl
        self.ant_ctrl = ant_ctrl

        
    def new_sim(self):
        self.simulation.reset()
        self.disable_sim()
        self.disable_save()
        self.start_page.show()
        

    def load_file(self):
        file_path = filedialog.askopenfilename(initialdir = "./Saves", title = "Load instance", filetypes = (("Ant File", "*.ant*"), ("all files","*.*")))
        
        self.ant_ctrl.load(file_path)
        
    def save_file(self):
        file_path = filedialog.asksaveasfilename(initialdir = "./Saves", title = "Save instance", filetypes = (("Ant File", "*.ant*"), ("all files","*.*")))

        if file_path[-4::] != ".ant":
            file_path += ".ant"
        self.ant_ctrl.save(file_path)


    def disable_sim(self):
        self.view.entryconfig("Simulation", state='disabled')

        
    def enable_sim(self):
        self.view.entryconfig("Simulation", state='normal')
    
    def disable_save(self):
        self.view.menu_file.entryconfig("Save", state='disabled')
        
    def enable_save(self):
        self.view.menu_file.entryconfig("Save", state='normal')        
        
    def step(self):
        self.simulation.step()

        
    def previous(self):
        self.simulation.previous()

        
    def play(self):
        self.simulation.play_forward()


    def reverse(self):
        self.simulation.play_reverse()
        
        
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
        self.menu_file = tk.Menu(self)
        self.menu_file.add_command(label="New", command=self.controller.new_sim)
        self.menu_file.add_command(label="Load", command=self.controller.load_file)
        self.menu_file.add_command(label="Save", command=self.controller.save_file)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Quit", command=self.master.destroy)

        self.add_cascade(menu=self.menu_file, label="File")

        self.menu_sim = tk.Menu(self)
        self.menu_sim.add_command(label="Next", command=self.controller.step)
        self.menu_sim.add_command(label="Previous", command=self.controller.previous)
        self.menu_sim.add_separator()
        self.menu_sim.add_command(label="Play", command=self.controller.play)
        self.menu_sim.add_command(label="Reverse", command=self.controller.reverse)
        self.menu_sim.add_command(label="Pause", command=self.controller.pause)
        self.menu_sim.add_separator()
        self.menu_sim.add_command(label="Reset", command=self.controller.reset)

        self.add_cascade(menu=self.menu_sim, label="Simulation")

        self.menu_help = tk.Menu(self)
        self.menu_help.add_command(label="Documentation", command=self.controller.documentation)
        self.menu_help.add_command(label="About", command=self.controller.about)
        self.add_cascade(menu=self.menu_help, label="Help")
