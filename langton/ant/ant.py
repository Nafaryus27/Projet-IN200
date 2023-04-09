import json

class Ant:
    def __init__(self, x:int, y:int, direction:int, rules:dict, world_size:int, default_color:str):
        """
        Initialise une fourmi de Langton avec les parametres suivants:
        
        :param int x: coordonnée abcisses fourmi
        :param int y: coordonnée ordonnées fourmi
        :param int direction: direction fourmi
        :param dict rules: regles (ex: {"white" :(1, "black"), "black": (-1, "white")})
        :param int world_size: taille de la grille
        :param str default_color: la couleur par default de la grille
        """

        self.x = x
        self.y = y
        self.direction = direction
        self.iteration = 0
        self.moves = [(0,-1),(1,0),(0,1),(-1,0)]
        
        self.rules = rules
        self.inverted_rules = {value[1]:(-value[0],key) for key, value in self.rules.items()}
        
        self.world_size = world_size
        self.world = [[default_color for i in range(self.world_size)] for j in range(self.world_size)]


    def iterate(self):
        """
        Permet de calculer l'iteration suivante de la fourmi de Langton
        a partir de regles fournies et de la position de la fourmi.
        """
        self.iteration += 1
        cell = self.world[self.y][self.x] 

        rotation, new_color = self.rules[cell]
        self.direction = (self.direction + rotation) % 4

        self.world[self.y][self.x] = new_color

        new_coordinates = self.moves[self.direction]

        self.x += new_coordinates[0] 
        self.y += new_coordinates[1]


        self.x %= self.world_size
        self.y %= self.world_size

        return (self.x, self.y, new_color)


    def iterate_previous(self):
        """
        Permet de calculer l'iteration précédante de la fourmi de Langton
        a partir de regles fournies et de la position de la fourmi.
        """
        self.iteration -= 1
        new_coordinates = self.moves[self.direction]

        self.x -= new_coordinates[0] 
        self.y -= new_coordinates[1]


        self.x %= self.world_size
        self.y %= self.world_size

        cell = self.world[self.y][self.x] 

        rotation, new_color = self.inverted_rules[cell]
        self.direction = (self.direction + rotation) % 4

        self.world[self.y][self.x] = new_color

        return (self.x, self.y, new_color)

    
    def save_data(self,save_name):
        data={"rules": self.rules,"x":self.x, "y":self.y,"direction":self.direction, "iteration":self.iteration}
        with open(save_name + ".json", "w") as file:
            json.dump(data, file)
            file.close()


    def save_world(self, save_name):
        with open(save_name + "_world.txt","w") as file:
            for l in self.world:
                file.write(" ".join(l) + "\n")
            file.close()
    
    
    def update_save_list(self, save_name):
        with open("save_list.txt","a+") as file:
            exist=False
            for line in file.readlines():
                if save_name in line:
                    exist=True
            if not exist:
                file.write(save_name + "\n")
            file.close()

    
    def save(self, save_name):
        self.update_save_list(save_name)
        self.save_data(save_name)
        self.save_world(save_name)

    
  

    

