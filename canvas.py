def initialisation_grille(Can,w:int,h:int,s:int):
    """
    crée une grille de h*w cases de tailles s pixel

    :param tkinter.Canvas Can: canvas sur lequel on dessine la grille
    :param int w:  nombre de case sur la largeur de la grille
    :param int h:  nombre de case sur la hauteur de la grille 
    :param int s:  taille d'une case en pixel 
    """
    for i in range(w): 
        for j in range(h):
            
            x=(i+1) * s
            y=(j+1) * s
            
            Can.create_rectangle(i*s,j*s,x,y,outline="black")
    return

        
def changer_couleur(Can,h:int,x:int,y:int,couleur:str):
    """
    permet de modifier la couleur de la case aux coordonées (x,y) dans la grille

    :param tkinter.Canvas Can: canvas contenant la grille
    :param int h:  nombre de case sur la hauteur de la grille 
    :param int x:  coordonée x de la case à modifier
    :param int y:  coordonées y de la case à modifier
    :param str couleur: nouvelle couleur de la case
    """
    Can.itemconfigure(x*h+y+1,fill = couleur)   
    

