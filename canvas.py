def dessiner_grille(can, n, s):
    indices=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            
            x=(i+1) * s
            y=(j+1) * s
            
            indices[i][j] = can.create_rectangle(i*s,j*s,x,y,outline="black")

    return indices