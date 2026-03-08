from tkinter.font import names
from game_object import GameObj, CharacterObj
import csv

class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = (15,15)
        self.start = ()
        self.exit = ()
        self.set_up()

    def set_up(self):
        self.set_background_from_file("background.csv")
        start_pos = (0, 7)
        self.player = CharacterObj("character", start_pos, "C")
        self.characters.append(self.player)

    def add_background_object(self, obj_type, name, btype, pos):
        if obj_type == "character":
            self.characters.append(CharacterObj(name, pos, btype))
        else:
            self.backgrounds.append(GameObj(name, pos, btype))

    def set_background_from_file(self, filename):
        with open(filename) as f:
            reader = csv.reader(f)

            for y, row in enumerate(reader):
                for x, cell in enumerate(row):

                    if cell == "W":
                        self.backgrounds.append(GameObj("wall", (x, y), "W"))

                    elif cell == "F":
                        self.backgrounds.append(GameObj("floor", (x, y), "F"))

                    elif cell == "S":
                        self.start = (x, y)
                        self.characters.append(CharacterObj("character", (x, y), "C"))

                    elif cell == "E":
                        self.exit = (x, y)
                        self.backgrounds.append(GameObj("exit", (x, y), "E"))

            self.dimensions = (len(row), y + 1)

    def check_collision(self, pos):
        contents = self.get_cell_contents(pos)

        for obj in contents:
            if obj.is_solid():
                return True

        return False

    def get_cell_contents(self, pos):
        objects = []

        for obj in self.backgrounds:
            if obj.pos == pos:
                objects.append(obj)

        for char in self.characters:
            if char.pos == pos:
                objects.append(char)

        return objects

    def move_character(self, character, direction):

        new_pos = character.find_next_location(direction)

        if not self.check_collision(new_pos):
            character.move(direction)
            return None
        else:
            return "The position you want to move to is solid"

    def find_objects_by_name(self, name):
        found = []

        for obj in self.backgrounds:
            if obj.name == name:
                found.append(obj)

        for char in self.characters:
            if char.name == name:
                found.append(char)

        return found

    def show_game_grid(self):
        width, height = self.dimensions
        grid_lines = []

        for y in range(height):
            row = []
            for x in range(width):
                pos = (x, y)
                contents = self.get_cell_contents(pos)

                if contents:
                    # Check if a character is in this cell
                    char_in_cell = next((c for c in contents if isinstance(c, CharacterObj)), None)
                    if char_in_cell:
                        row.append("C")
                    else:
                        obj = contents[0]
                        if obj.btype == "W":
                            row.append("▓")
                        elif obj.btype == "F":
                            row.append(".")
                        elif obj.btype == "E":
                            row.append("E")
                        else:
                            row.append(obj.name[0])
                else:
                    row.append(".")  # empty cell

            grid_lines.append("".join(row))

        return "\n".join(grid_lines)