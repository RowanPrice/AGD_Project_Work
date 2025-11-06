import random

def dice_sum(num_dice:int = 1,num_sides:int = 6):
    """returns the sum of num_dice dice, each with num_sides sides"""
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

class Character:

    def __init__(self, name:str , skill:int , stamina:int):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def find_score(self):
        self.roll = dice_sum(2,6)
        self.score = self.skill + self.roll

    def take_hit(self, damage=2):
        self.stamina -= damage

    def fight_round(self,other):
        self.find_score()
        other.find_score()
        if other.score > self.score:
            result = 'lost'
            self.take_hit()
        elif other.score < self.score:
            result = 'won'
            other.take_hit()
        else:
            result = 'draw'
            self.take_hit(1)
            other.take_hit(1)
        return result

    def return_character_status(self):
        return f"{self.name} has {self.skill} skill and {self.stamina} stamina"

    def return_roll_status(self):
        return f"{self.name} rolled {self.roll} for a total score of {self.score}"



    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self,dead:bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)

class PlayerCharacter(Character):
    def __init__(self, name: str, skill: int, stamina: int, luck: int):
        super().__init__(name, skill, stamina)
        self.luck = luck

    @classmethod
    def generate_player_character(cls,name):
        skill = dice_sum(2,6)
        stamina = dice_sum(2,6)
        luck = dice_sum(2,6)
        return cls(name, skill, stamina, luck)

    def __repr__(self):
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    def test_luck(self):
        roll = dice_sum(2,6)
        if roll <= self.luck:
            self.luck -= 1
            self.roll = roll
            return True
        else:
            self.luck -= 1
            self.roll = roll
            return False

class NPCCharacter(Character):
    def __init__(self, name: str, skill: int, stamina: int, ):
        super().__init__(name,skill,stamina)

class Game:

    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures

    @classmethod
    def load_creatures(cls):
        creatures = [Character("Dragon",10,22),
                     Character("Orc",7,10),
                     Character("Skeleton",5,8),
                     Character("Large rat",6,6),]

    def return_round_result(self, other):
        msg = self.return_character_status()
        msg2 = other.return_character_status()
        if self.fight_round(other) == 'won':
            return f"{msg}\n{msg2}\n{self.name} won"
        elif self.fight_round(other) == 'lost':
            return f"{msg}\n{msg2}\n{self.name} lost"
        else:
            return f"{msg}\n{msg2}\n{self.name} drew"

pc = Character('jim',skill=3,stamina=4)
orc = Character('orc',skill=5,stamina=2)