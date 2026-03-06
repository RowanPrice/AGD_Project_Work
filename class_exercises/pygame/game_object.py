from game_controller import Game

class GameObj:
    def __init__(self,name,pos,btype):
        self.name = name
        self.pos = pos
        self.btype = btype

    def __str__(self):
        return f'Name="{self.name}", Pos={self.pos}, Btype="{self.btype}"'

    def is_solid(self):
        if self.btype == 'W' or self.btype == 'C':
            return True
        else:
            return False

class CharacterObj(GameObj):
    def find_next_location(self,direction):
        if direction == 'right':
            return self.pos[0] + 1, self.pos[1]
        elif direction == 'left':
            return self.pos[0] - 1, self.pos[1]
        elif direction == 'down':
            return self.pos[0], self.pos[1] + 1
        else:
            return self.pos[0], self.pos[1] - 1

    def move(self,direction):
        if direction == 'right':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif direction == 'left':
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif direction == 'down':
            self.pos = (self.pos[0], self.pos[1] + 1)
        else:
            self.pos = (self.pos[0], self.pos[1] - 1)