

import tkinter as tk


def grille(Can,n,s): #definition d'une grille 
    
    for i in range(1,n): #on met à 1 pour avoir les rectangles bien numerotés
        for j in range(1,n):
            
            x=(i+1) * s
            y=(j+1) * s
            
            Can.create_rectangle(i*s,j*s,x,y,outline="black")
    return

        

### fonction pour changer la couleur d'un rectangle

def changer_couleur(Can,h,x,y,couleur):
    Can.itemconfigure(x*h+y+1,fill = couleur)   #Can.itemconfigure
    

