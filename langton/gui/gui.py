import tkinter as tk
from tkinter import ttk
from .startpage import StartPageCTRL
from .simview import SimulationViewCTRL
from .menubar import MenuBarCTRL

class LangtonGUI(tk.Tk):
    def __init__(self, app):
        tk.Tk.__init__(self)

        self.app = app
        self.title("Langton's ant")
        self.geometry('1920x1080')

        style = ttk.Style(self)
        style.theme_use('clam')        
        self.option_add('*tearOff', False)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.init_widgets()

    def init_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        self.simulation_ctrl = SimulationViewCTRL(main_frame, self)
        self.start_page_ctrl = StartPageCTRL(main_frame, self.app, self.simulation_ctrl)
        
        self.menu_bar = MenuBarCTRL(self, self.app, self.start_page_ctrl, self.simulation_ctrl)
        self.simulation_ctrl.set_menu(self.menu_bar)

        
    def set_model(self, model):
        self.model = model
        self.simulation_ctrl.set_model(model)
        self.start_page_ctrl.set_model(model)
        

