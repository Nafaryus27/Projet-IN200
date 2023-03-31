import tkinter as tk
from tkinter import ttk
from viewer import Viewer

class LangtonGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Langton's ant")
        self.geometry('1920x1080')

        style = ttk.Style(self)
        style.theme_use('clam')        
        self.option_add('*tearOff', False)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.init_widgets()

    def init_widgets(self):
        menu_bar = MenuBar(self)
        self['menu'] = menu_bar
    
        main_frame = ttk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        ctrl_start_page = StartPageCTRL(self, model),
        ctrl_simulation_view = SimulationViewCTRL(self, model)
        

class StartPageCTRL:
    def __init__(self, parent, model):
        self.view = StartPage(parent, self)
        self.model = model

    def show(self):
        self.view.tkraise()
        
    def launch_callback(self):
        pass

    def get_rule(self):
        return self.view.rule_entry.get_rule()

        
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid(row=0, column=0, sticky="news")
       
        self.init_widgets()


    def init_widgets(self):
        cont = ttk.Frame(self)
        cont.grid(row=1, column=1)

        self.rule_entry = LabeledEntry(cont, "Rule", "RL")
        
                
        launch_button = ttk.Button(cont, text="Launch", command=self.controller.launch_callback)
        load_button = ttk.Button(cont, text="Load", command=load_file)

        rule_entry.grid(row=0, column=0, sticky='news')
        launch_button.grid(row=3, column=0, sticky='news')
        load_button.grid(row=4, column=0, sticky='news')


class SimulationViewCTRL:
    def __init__(self, parent, controller):
        self.view = SimulationView(parent, self)
        self.model = model
    
    def sim_next(self):
        pass

    def sim_previous(self):
        pass

    def sim_play(self):
        pass

    def sim_pause(self):
        pass

    def sim_reset(self):
        pass

    
class SimulationView(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        tool_bar = ToolBar(self)
        tool_bar.grid(row=0, column=0, sticky='ew')

        self.viewer = Viewer(self, 900, 900, 15)
        self.viewer.grid(row=1, column=1, sticky='news')

        
class LabeledEntry(ttk.Frame):
    def __init__(self, master, text:str, default_value:str):
        ttk.Frame.__init__(self, master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.value = tk.StringVar(self, default_value)

        self.init_widgets(text, default_value)
        
    def init_widgets(self, text:str, default_value:str):
        label = ttk.Label(self, text=text)
        label.grid(row=0, column=0, sticky='e')
        
        entry = ttk.Entry(self, textvariable=self.value)
        entry.grid(row=0, column=1)
        
        self.get = entry.get

                      
class ToolBar(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        
        button = ttk.Button(self, text="Test")
        button.grid()

        
class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        self.controller = master
        self.init_widgets()
        
    def init_widgets(self):
        menu_file = tk.Menu(self)
        menu_file.add_command(label="New", command=new_file)
        menu_file.add_command(label="Load", command=load_file)
        menu_file.add_command(label="Save", command=save_file)
        menu_file.add_command(label="Close", command=close_file)
        menu_file.add_separator()
        menu_file.add_command(label="Settings", command=settings)
        menu_file.add_command(label="Quit", command=self.master.destroy)

        self.add_cascade(menu=menu_file, label="File")

        menu_sim = tk.Menu(self)
        menu_sim.add_command(label="Next", command=sim_next)
        menu_sim.add_command(label="Previous", command=sim_previous)
        menu_sim.add_separator()
        menu_sim.add_command(label="Play", command=sim_play)
        menu_sim.add_command(label="Pause", command=sim_pause)
        menu_sim.add_separator()
        menu_sim.add_command(label="Reset", command=sim_reset)

        self.add_cascade(menu=menu_sim, label="Simulation")

        menu_help = tk.Menu(self)
        menu_help.add_command(label="Documentation", command=documentation)
        menu_help.add_command(label="About", command=about)
        self.add_cascade(menu=menu_help, label="Help")


def new_file():
    pass


def load_file():
    pass


def close_file():
    pass


def save_file():
    pass


def settings():
    pass


def sim_next(self):
    pass

def sim_previous(self):
    pass

def sim_play(self):
    pass

def sim_pause(self):
    pass

def sim_reset(self):
    pass

def documentation():
    pass


def about():
    pass
