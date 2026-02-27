from tkinter.font import names


class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = ()
        self.start = ()
        self.exit = ()

    def set_up(self):
        pass

    def add_background_object(self,btype,pos):
        if btype == 'W':

    def set_background_from_file(self,background_file):
        pass

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

class GameObj(Game):
    def __init__(self,name,pos,btype):
        self.name = name
        self.pos = pos
        self.btype = btype