import tkinter as tk

class Viewer(tk.Canvas):
    def __init__(self, master, cs):
        """
        Initialisation du canvas sur lequel la fourmie évolue

        avec :
        self.grid_w: largeur de la grille (en nombre de cases)
        self.grid_h: hauteur de la grille (en nombre de cases)
        self.cell_size: taille d'une case en pixelsw

        :param master: widget parent du canvas
        :param cs: taille en pixels des cases de la grille
        """
        tk.Canvas.__init__(self, master, height=940, width=1920)

        self.cell_size = cs
        self.grid_h = int(self['height']) // self.cell_size
        self.grid_w = int(self['width']) // self.cell_size

        self.grid_init()

        
    def grid_init(self):
        """
        initialisation de la grille de h*w cases de tailles s pixels      
        """
        for i in range(self.grid_w): 
            for j in range(self.grid_h):
                x = (i + 1) * self.cell_size
                y = (j + 1) * self.cell_size            
                self.create_rectangle(i * self.cell_size, j * self.cell_size, x, y, outline="grey")
        return

            
    def set_color(self,x:int,y:int,couleur:str):
        """
        permet de modifier la couleur de la case aux coordonées (x,y) dans la grille
                
        :param int x:  coordonée x de la case à modifier
        :param int y:  coordonées y de la case à modifier
        :param str couleur: nouvelle couleur de la case
        """
        self.itemconfigure(x*self.grid_h+y+1,fill = couleur)    

