from . import gui, ant

class Langton:
    def __init__(self):
        self.GUI = gui.LangtonGUI(self)
        
    def new_ant(self, x:int, y:int, direction:int, rules:dict, world_size:int, default_color:str):
        self.ant = ant.Ant(x, y, direction, world_size, default_color)
        self.GUI.set_model(ant)

    def run(self):
        self.GUI.mainloop()
