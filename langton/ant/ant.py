class Ant:
    def __init__(self, x:int=0, y:int=0, direction:int=0, rules:dict={}, world_size:int=0, default_color:str=""):
        """
        Initialise une fourmi de Langton avec les parametres suivants:
        
        :param int x: coordonnée abcisses fourmi
        :param int y: coordonnée ordonnées fourmi
        :param int direction: direction fourmi
        :param dict rules: regles (ex: {"white" :(1, "black"), "black": (-1, "white")})
        :param int world_size: taille de la grille
        :param str default_color: la couleur par default de la grille
        """
        self.start_pos = (x,y, direction)
        self.default_color = default_color
        
        self.x = x
        self.y = y
        self.direction = direction
        self.iteration = 0
        
        self.moves = [(0,-1),(1,0),(0,1),(-1,0)]
        self.rules = rules
        self.inverted_rules = {value[1]:(-value[0],key) for key, value in self.rules.items()}
        
        self.world_size = world_size
        self.world = [[self.default_color for i in range(self.world_size)] for j in range(self.world_size)]


    def iterate(self):
        """
        Permet de calculer l'iteration suivante de la fourmi de
        Langton a partir de regles fournies et de la position de la
        fourmi.
        """
        self.iteration += 1
        cell = self.world[self.y][self.x] 

        rotation, new_color = self.rules[cell]
        self.direction = (self.direction + rotation) % 4

        self.world[self.y][self.x] = new_color

        new_coordinates = self.moves[self.direction]
        oldx, oldy = self.x, self.y
        self.x += new_coordinates[0] 
        self.y += new_coordinates[1]


        self.x %= self.world_size
        self.y %= self.world_size

        return (oldx, oldy, new_color)


    def iterate_previous(self):
        """
        Permet de calculer l'iteration précédante de la fourmi de
        Langton a partir de regles fournies et de la position de la
        fourmi.
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


    def reset(self):
        self.x, self.y, self.direction= self.start_pos
        self.world = [[self.default_color for i in range(self.world_size)] for j in range(self.world_size)]

    
    def get_data(self):
        """
        Renvoie les information de la fourmi sous la forme d'un
        dictionnaire
        """
        data={"rules": self.rules,
              "inverted_rules": self.inverted_rules,
              "x": self.x,
              "y": self.y,
              "direction": self.direction,
              "start_pos": self.start_pos,
              "iteration": self.iteration,
              "default_color": self.default_color,
              "world_size": self.world_size,
              "world": self.world}
        return data

    def load_from_data(self, data:dict):
        """
        Créée une fourmi à partir de data
        """
        self.rules = data['rules']
        self.inverted_rules = data['inverted_rules']
        self.x = data['x']
        self.y = data['y']
        self.direction = data['direction']
        self.start_pos = data['start_pos']
        self.iteration = data['iteration']
        self.default_color = data['default_color']
        self.world_size = data['world_size']
        self.world = data['world']
        return(self)

