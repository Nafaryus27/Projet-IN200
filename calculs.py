def bouger(pos, dir, items): #position et direction (cardinaux)
    i, j = pos  #position par rapport a ses coordonnées (lignes, colonnes)

    if items[i][j] == 0: #si la couleur de la case est claire
        if dir == "N":
            r = (i, j + 1), "E" "est"
        elif dir == "S":
            r = (i, j - 1), "W" "ouest"
        elif dir == "E":
            r = (i + 1, j), "S" "sud" #une ligne en dessous et la même colonne
        elif dir == "W":
            r = (i - 1, j), "N" "nord"
    else:  #case sombre
        if dir == "S":  
            r = (i, j + 1), "E"  
        elif dir == "N":
            r = (i, j - 1), "W"
        elif dir == "W":
            r = (i + 1, j), "S" 
        elif dir == "E":
            r = (i - 1, j), "N"
    return r #r est un couple (npos (nouvelle position couple ligne x colonne), ndir (nouvelle direction (donc parmi "N", "S", "E" et "W"))


#Par exemple, si i=42, j=81 , dir="W" et la case (i, j) est noire alors la fourmi se déplace à sa gauche (donc vers la bas), donc sa nouvelle position est (42, 82) et sa nouvelle direction est "S".