import tkinter as tk
from tkinter import ttk


class LangtonsAntApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1920x1080')

        self.option_add('*tearOff', False)
        menu_bar = MenuBar(self)
        self['menu'] = menu_bar

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_frame = ttk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=0)
        main_frame.grid_rowconfigure(1, weight=1)

        tool_bar = ToolBar(main_frame)
        tool_bar.grid(row=0, column=0, sticky="w")

        start = StartupPage(main_frame, self)
        start.grid(row=1, column=0, sticky="news")

        # view = Viewer(main_frame, height=400, width=400, bg="black",)
        # view.grid(row=1, column=0)


class StartupPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, relief='ridge', width=200, height=100)


class ToolBar(ttk.Frame):

    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        button = ttk.Button(self, text='Test')
        button.grid()


class Viewer(tk.Canvas):

    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)


class MenuBar(tk.Menu):

    def __init__(self, *args, **kwargs):
        tk.Menu.__init__(self, *args, **kwargs)

        menu_file = tk.Menu(self)
        menu_file.add_command(label='New', command=new_file)
        menu_file.add_command(label='Open...', command=open_file)
        menu_file.add_command(label='Save', command=save_file)
        menu_file.add_command(label='Close', command=close_file)
        menu_file.add_separator()
        menu_file.add_command(label='Settings', command=settings)
        menu_file.add_command(label='Quit', command=args[0].destroy)

        self.add_cascade(menu=menu_file, label='File')

        menu_sim = tk.Menu(self)
        menu_sim.add_command(label='Next', command=sim_next)
        menu_sim.add_command(label='Previous', command=sim_previous)
        menu_sim.add_separator()
        menu_sim.add_command(label='Play', command=sim_play)
        menu_sim.add_command(label='Pause', command=sim_pause)
        menu_sim.add_separator()
        menu_sim.add_command(label='Reset', command=sim_reset)

        self.add_cascade(menu=menu_sim, label='Simulation')

        menu_help = tk.Menu(self)
        menu_help.add_command(label='Documentation', command=documentation)
        menu_help.add_command(label='About', command=about)
        self.add_cascade(menu=menu_help, label='Help')


def new_file():
    pass


def open_file():
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
