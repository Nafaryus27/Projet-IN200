import tkinter as tk
from tkinter import ttk
from .startpage import StartPageCTRL
from .simview import SimulationViewCTRL
from .menubar import MenuBarCTRL
from .doc import DocumentationPageCTRL

class LangtonGUI(tk.Tk):
    def __init__(self, model_ctrl):
        """
        Classe principale de l'interface graphique. Contient les
        différentes pages (start, simulation, documentation) de
        l'application
        
        :param model_ctrl: controlleur du model
        """
        tk.Tk.__init__(self)

        self.model_ctrl = model_ctrl
        self.title("Langton's ant")
        self.geometry('1920x1080')

        style = ttk.Style(self)
        style.theme_use('clam')        
        self.option_add('*tearOff', False)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.about_msg_path = "doc/about.html"
        self.doc_path = "doc/documentation.html"
        
        self.init_widgets()

    def init_widgets(self):
        """
        Initialisation des différentes pages et de la
        barre de menu
        """
        
        self.top_frame = None
        
        main_frame = ttk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        self.menu_bar = MenuBarCTRL(self, self.model_ctrl, about_msg_path=self.about_msg_path)
        self.simulation_ctrl = SimulationViewCTRL(main_frame, controller=self, root=self)
        self.start_page_ctrl = StartPageCTRL(main_frame, controller=self, model_ctrl=self.model_ctrl, simulation_ctrl=self.simulation_ctrl)
        self.doc_page_ctrl = DocumentationPageCTRL(main_frame, controller=self, doc_path=self.doc_path)

        self.menu_bar.set_start_page_ctrl(self.start_page_ctrl)
        self.menu_bar.set_simulation_ctrl(self.simulation_ctrl)
        self.menu_bar.set_doc_page_ctrl(self.doc_page_ctrl)

        self.simulation_ctrl.set_menu(self.menu_bar)
        self.start_page_ctrl.show()
        
        
    def set_model(self, model):
        self.model = model
        self.simulation_ctrl.set_model(model)
        self.start_page_ctrl.set_model(model)
        

    def set_top_frame(self, frame):
        self.top_frame = frame
