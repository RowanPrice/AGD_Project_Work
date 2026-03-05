from tkinter.font import names


class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = ()
        self.start = ()
        self.exit = ()

    def set_up(self):
        self.set_background_from_file("background.txt")
        self.add_background_object('character', 'C', 'C', (1, 9))

    def add_background_object(self,type,name,btype,pos):
        if type == "character":
            self.characters.append(CharacterObj(name, pos, btype))
        else:
            self.backgrounds.append(GameObj(name, pos, btype))

    def set_background_from_file(self, background_file):
        with open(background_file, "r") as file:
            for line in file:
                name, pos, btype = line.strip().split()
                pos = pos.strip("()")
                x, y = pos.split(",")
                pos = (int(x), int(y))

                self.backgrounds.append(GameObj(name, pos, btype))

    def check_collision(self,pos):
        pass

    def get_cell_contents(self,pos):
        pass

    def move_character(self,character,pos):
        pass

    def find_objects_by_name(self,name):
        pass

    def show_game_grid(self):
        pass

class GameObj:
    def __init__(self,name,pos,btype):
        self.name = name
        self.pos = pos
        self.btype = btype

    def __str__(self):
        return f'Name:{self.name} Pos:{self.pos} Btype:{self.btype}'

    def is_solid(self):
        if self.btype == 'W':
            return True
        else:
            return False

class CharacterObj(GameObj):
    def find_next_location(self,direction):
        if direction == 'right':
            return self.pos[0] + 1, self.pos[1]
        elif direction == 'left':
            return self.pos[0] - 1, self.pos[1]
        elif direction == 'up':
            return self.pos[0], self.pos[1] + 1
        else:
            return self.pos[0], self.pos[1] - 1

    def move(self,direction):
        if direction == 'right':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif direction == 'left':
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif direction == 'up':
            self.pos = (self.pos[0], self.pos[1] + 1)
        else:
            self.pos = (self.pos[0], self.pos[1] - 1)