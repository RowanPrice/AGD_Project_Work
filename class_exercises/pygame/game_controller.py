from tkinter.font import names
from game_object import GameObj, CharacterObj


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

    def add_background_object(self, obj_type, name, btype, pos):
        if obj_type == "character":
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

        if not self.check_collision(pos):
            character.move(pos)
            return None
        else:
            return 'The position you want to move to is solid'

    def find_objects_by_name(self,name):
        pass

    def show_game_grid(self):
        pass