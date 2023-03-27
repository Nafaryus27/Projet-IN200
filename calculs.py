def iterate_ant(world :list, rules :dict, x :int, y :int, dir_id :int, reverse :bool = False):
    """
    Permet de calculer l'iteration suivante de la fourmi de Langton
     a partir de regles fournies et de la position de la fourmi. 

     param list world: grille
     param dict rules: regles 
     param int x: coordonnée abcisses fourmi
     param int y: coordonnée ordonnées fourmi
     param int dir_id: direction fourmi 
    """
    direction = "NESW"
    rotation = {"R":1, "L":-1}
    M = {"N":(0,-1),"S":(0,1), "E":(1,0), "W":(-1,0)}
    cell = world[y][x] 

    r, new_color = rules[cell]
    dir_id = (dir_id + rotation[r]) % 4

    world[y][x]= new_color

    nc = M[direction[dir_id]]

    x += nc[0] 
    y += nc[1]


    x %= len(world[0])
    y %= len(world)

    return (dir_id, x, y)




