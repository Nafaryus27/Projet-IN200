import tkinter as tk
from tkinter import ttk

class LabeledEntry(ttk.Frame):
    def __init__(self, master, var_type, text:str, default_value:str):
        ttk.Frame.__init__(self, master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.value = var_type(self, default_value)

        self.init_widgets(text, default_value)
        
    def init_widgets(self, text:str, default_value:str):
        label = ttk.Label(self, text=text)
        label.grid(row=0, column=0, sticky='e')
        
        entry = ttk.Entry(self, textvariable=self.value)
        entry.grid(row=0, column=1)
        
        self.get = entry.get

class LabeledEntryStr(LabeledEntry):
    def __init__(self, master, text:str, default_value:str):
        LabeledEntry.__init__(self, master, tk.StringVar, text, default_value)

class LabeledEntryInt(LabeledEntry):
    def __init__(self, master, text:str, default_value:str):
        LabeledEntry.__init__(self, master, tk.IntVar, text, default_value)
        
                      
class ToolBar(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        button = ttk.Button(self, text="Test")
        button.grid()
