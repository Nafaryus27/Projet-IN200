import tkinter as tk
from tkinter import ttk, filedialog
from .doc import AboutPopup

class MenuBarCTRL:
    def __init__(self, master, model_ctrl, about_msg_path:str, start_page_ctrl=None, simulation_view_ctrl=None, doc_page_ctrl=None):
        """
        Initialisation du controlleur de la barre de menus

        :param master: widget parent de la barre de menus
        :param model_ctrl: controlleur du model
        :param str about_msg_path: chemin vers le message affiché par
        la popup dans "About"
        :param start_page_ctrl: controlleur de la page de démarrage
        :param simulation_view_ctrl: controlleur de la vue de simulation
        :param doc_page_ctrl: controlleur de la page de documnetation
        """
        self.view = MenuBar(master, self)
        self.disable_sim()
        self.disable_save()
        self.model_ctrl = model_ctrl
        self.simulation_view_ctrl = simulation_view_ctrl
        self.start_page_ctrl = start_page_ctrl
        self.doc_page_ctrl = doc_page_ctrl
        self.about_popup = AboutPopup(about_msg_path)
        
    def set_start_page_ctrl(self, start_page_ctrl):
        self.start_page_ctrl = start_page_ctrl

        
    def set_simulation_view_ctrl(self, simulation_view_ctrl):
        self.simulation_view_ctrl = simulation_view_ctrl

        
    def set_model_ctrl(self, model_ctrl):
        self.model_ctrl = model_ctrl


    def set_doc_page_ctrl(self, doc_page_ctrl):
        self.doc_page_ctrl = doc_page_ctrl

        
    def new_sim(self):
        self.simulation_view_ctrl.reset()
        self.disable_sim()
        self.disable_save()
        self.start_page_ctrl.show()
        

    def load_file(self):
        file_path = filedialog.askopenfilename(initialdir = "./Saves", title = "Load instance", filetypes = (("Ant File", "*.ant*"), ("all files","*.*")))
        if file_path:
            self.model_ctrl.load(file_path)

        
    def save_file(self):
        file_path = filedialog.asksaveasfilename(initialdir = "./Saves", title = "Save instance", filetypes = (("Ant File", "*.ant*"), ("all files","*.*")))

        if file_path:
            if file_path[-4::] != ".ant":
                file_path += ".ant"
            self.model_ctrl.save(file_path)


    def disable_sim(self):
        self.view.entryconfig("Simulation", state='disabled')

        
    def enable_sim(self):
        self.view.entryconfig("Simulation", state='normal')
    
    def disable_save(self):
        self.view.menu_file.entryconfig("Save", state='disabled')
        
    def enable_save(self):
        self.view.menu_file.entryconfig("Save", state='normal')        
        
    def step(self):
        self.simulation_view_ctrl.step()

        
    def previous(self):
        self.simulation_view_ctrl.previous()

        
    def play(self):
        self.simulation_view_ctrl.play_forward()


    def reverse(self):
        self.simulation_view_ctrl.play_reverse()
        
        
    def pause(self):
        self.simulation_view_ctrl.pause()

        
    def reset(self):
        self.simulation_view_ctrl.reset()

        
    def documentation(self):
        self.doc_page_ctrl.show()

    
    def about(self):
        self.about_popup.popup()

    
class MenuBar(tk.Menu):
    def __init__(self, master, controller):
        tk.Menu.__init__(self, master)

        self.controller = controller
        self.init_widgets()
        master['menu'] = self

        
    def init_widgets(self):
        """
        Inialisation des catégories et menus 
        """
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
