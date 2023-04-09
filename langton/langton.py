from . import gui, ant

class Langton:
    def __init__(self):
        self.GUI = gui.LangtonGUI(self)
        
    def new_ant(self, x:int, y:int, direction:int, rules:dict, world_size:int, default_color:str):
        self.Ant = ant.Ant(x, y, direction, rules, world_size, default_color)
        self.GUI.set_model(self.Ant)

    def run(self):
        self.GUI.mainloop()
