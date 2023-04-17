from . import gui, ant
import json

class Langton:
    def __init__(self):
        """
        classe permettant de lancer l'application
        Joue aussi le rôle de controlleur du model (création
        et sauvegardes / chargement)
        """
        self.GUI = gui.LangtonGUI(self)
        
    def new_ant(self, x:int, y:int, direction:int, rules:dict, world_size:int, default_color:str):
        self.Ant = ant.Ant(x, y, direction, rules, world_size, default_color)
        self.GUI.set_model(self.Ant)
        return

    def save(self, file_path:str):
        """
        Permet de sauvegarder les informations de instance de la
        fourmi en cours au format json (position, orientation, les
        règles, l'itération, la grille)

        :param str file_path: chemin d'accès du fichier json
        """
        if file_path:
            with open(file_path, "w") as f:
                data = self.Ant.get_data()
                json.dump(data, f)
                f.close()


    def load(self, file_path):
        """
        Permet de charger une instance précédement sauvegardée au
        format json

        :param str file_path: chemin d'accès du fichier json
        """
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
                self.Ant = ant.Ant().load_from_data(data)
                f.close()
            self.GUI.set_model(self.Ant)
            self.GUI.simulation_view_ctrl.load(self.Ant.world)
            
        
    def run(self):
        self.GUI.mainloop()
