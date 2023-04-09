import tkinter as tk

class Viewer(tk.Canvas):
    def __init__(self, master, height:int, width:int, grid_size:int, default_color:str):
        """
        Initialisation du canvas sur lequel la fourmie évolue

        :param master: widget parent du canvas
        :param int width: largeur de canvas (en pixels)
        :param int height: hauteur du canvas (en pixels)
        :param int grid_size: dimension de la grille (en nombre de cases)
        """
        
        tk.Canvas.__init__(self, master, width=width + 1, height=height + 1)
        self.default_color = default_color
        self.grid_size = grid_size
        self.cell_size = height // grid_size
        self.grid_init()

        
    def grid_init(self):
        """
        initialisation de la grille de h*w cases de tailles s pixels      
        """
        for i in range(self.grid_size): 
            for j in range(self.grid_size):
                x = (i + 1) * self.cell_size
                y = (j + 1) * self.cell_size          
                self.create_rectangle(i * self.cell_size + 1, j * self.cell_size + 1, x + 1, y + 1, outline="grey", fill=self.default_color)
        return

            
    def set_color(self, x:int, y:int, color:str):
        """
        permet de modifier la couleur de la case aux coordonées (x,y) dans la grille
                
        :param int x:  coordonée x de la case à modifier
        :param int y:  coordonées y de la case à modifier
        :param str couleur: nouvelle couleur de la case
        """
        self.itemconfigure(x*self.grid_size+y+1,fill = color)    



    def reset(self):
        for i in range(self.grid_size ** 2):
            self.itemconfigure(i+1, fill = self.default_color)
