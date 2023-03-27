def bouger(pos, dir, items,n): #position et direction (cardinaux)
    y, x = pos  #position par rapport a ses coordonnées (lignes, colonnes)

    if items[y][x] == 0: #si la couleur de la case est claire
        if dir == "N":
            x += 1
            ndir = "E" #est
        elif dir == "S":
            x -= 1
            ndir="W" #ouest
        elif dir == "E":
            y += 1
            ndir= "S" #sud #une ligne en dessous et la même colonne
        elif dir == "W":
            y -= 1
            ndir= "N" #nord
        items[y][x] = 1
    else:  #case sombre
        if dir == "S":  
            x += 1
            ndir= "E"  
        elif dir == "N":
            x -= 1
            ndir= "W"
        elif dir == "W":
            y += 1
            ndir= "S" 
        elif dir == "E":
            y -= 1
            ndir= "N"
        items[y][x] = 0
    y %= n
    x %= n

    return x,y,ndir #r est un couple (npos (nouvelle position couple ligne x colonne), ndir (nouvelle direction (donc parmi "N", "S", "E" et "W"))


#Par exemple, si y=42, x=81 , dir="W" et la case (y, x) est noire alors la fourmi se déplace à sa gauche (donc vers la bas), donc sa nouvelle position est (42, 82) et sa nouvelle direction est "S".