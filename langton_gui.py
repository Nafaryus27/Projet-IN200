import tkinter as tk
from tkinter import ttk


class LangtonsAntApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Langton's ant")
        self.geometry('1920x1080')

        style = ttk.Style(self)
        style.theme_use('clam')        
        
        self.option_add('*tearOff', False)
        menu_bar = MenuBar(self)
        self['menu'] = menu_bar

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_frame = ttk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        self.pages = {}
        
        for F in (StartupPage, SimulationView):
            frame = F(main_frame, self)
            self.pages[F] = frame
            
            frame.grid(row=0, column=0, sticky="news")

        self.show(StartupPage)

    def show(self, p):
        page = self.pages[p]
        if p == SimulationView:
            w,h,r = self.pages[StartupPage].get_input_values()
            page.launch(w,h,r)
        page.tkraise()


class StartupPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) 

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        cont = ttk.Frame(self)
        cont.grid(row=1, column=1)

        self.rule_label = ttk.Label(cont, text="Rule")
        self.rule_label.grid(row=0, column=0, sticky='e')
        self.rule_val = tk.StringVar(self)
        self.rule_val.set("RL")
        self.rule_input = ttk.Entry(cont, textvariable=self.rule_val)
        self.rule_input.grid(row=0, column=1)

        
        launch_button = ttk.Button(cont, text="Launch", command=lambda : controller.show(SimulationView))
        launch_button.grid(row=3, column=0, columnspan=2, sticky='news')

        load_button = ttk.Button(cont, text="Load", command=load_file)
        load_button.grid(row=4, column=0, columnspan=2, sticky='news')

    def get_input_values(self):
        return(self.rule_input.get())


class LabeledEntry(ttk.Frame):
    def __init__(self, parent, text:str, default_value:str):
        ttk.Frame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        


    def get(self):
        return(self._input.get())

    def set(self, value):
        self.val.set(value)

    
class SimulationView(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tool_bar = ToolBar(self, relief='ridge')
        tool_bar.grid(row=0, column=0, sticky='ew')

    def launch(self, w, h, r):
        view = Viewer(self, bg='black')
        view.grid(row=1, column=0, sticky='news')

    

        
class Viewer(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        

                      
class ToolBar(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        
        button = ttk.Button(self, text="Test")
        button.grid()

class MenuBar(tk.Menu):

    def __init__(self, *args, **kwargs):
        tk.Menu.__init__(self, *args, **kwargs)

        menu_file = tk.Menu(self)
        menu_file.add_command(label="New", command=new_file)
        menu_file.add_command(label="Load", command=load_file)
        menu_file.add_command(label="Save", command=save_file)
        menu_file.add_command(label="Close", command=close_file)
        menu_file.add_separator()
        menu_file.add_command(label="Settings", command=settings)
        menu_file.add_command(label="Quit", command=args[0].destroy)

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


def sim_next():
    pass


def sim_previous():
    pass


def sim_play():
    pass


def sim_pause():
    pass


def sim_reset():
    pass


def documentation():
    pass


def about():
    pass
