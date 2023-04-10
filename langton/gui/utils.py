import tkinter as tk
from tkinter import ttk

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
        
        self.entry = ttk.Entry(self, textvariable=self.value)
        self.entry.grid(row=0, column=1)
        
    def get(self):
        return self.entry.get()

class LabeledSpinbox(ttk.Frame):
    def __init__(self, master, text:str, default_value:int, variable_name:str="", callback=None):
        ttk.Frame.__init__(self, master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.value = tk.IntVar(self, default_value, name=variable_name) if variable_name else tk.IntVar(self, default_value)
        if callback:
            self.value.trace("w", callback)
        self.init_widgets(text, default_value)
        
    def init_widgets(self, text:str, default_value:int):
        label = ttk.Label(self, text=text)
        label.grid(row=0, column=0, sticky='e')
        
        self.entry = ttk.Spinbox(self, textvariable=self.value, from_=1, to=1000)
        self.entry.grid(row=0, column=1)
        
    def get(self):
        return self.entry.get()
        
class ToolBar(ttk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.controller  = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        cont = ttk.Frame(self)
        button_next = ttk.Button(cont, text="Next", command=self.controller.step)
        button_previous = ttk.Button(cont, text="Previous", command=self.controller.previous)
        button_play = ttk.Button(cont, text="Play", command=self.controller.play_forward)
        button_reverse = ttk.Button(cont, text="Reverse", command=self.controller.play_reverse)
        button_pause = ttk.Button(cont, text="Pause", command=self.controller.pause)
        self.speed_entry = LabeledSpinbox(cont, text="Speed (in ms)", default_value=1, variable_name="speed", callback=self.spinbox_callback)
        button_reset = ttk.Button(cont, text="Reset", command=self.controller.reset)

        button_next.grid(row=0,column=0)
        button_previous.grid(row=0, column=1)
        button_play.grid(row=0, column=2)
        button_reverse.grid(row=0, column=3)
        button_pause.grid(row=0, column=4)
        button_reset.grid(row=0, column=5)
        self.speed_entry.grid(row=0,column=6)
        cont.grid(row=0, column=1, sticky='news')
        
    def spinbox_callback(self, *args):
        if self.speed_entry.get():
            self.controller.set_speed(self.speed_entry.get())
