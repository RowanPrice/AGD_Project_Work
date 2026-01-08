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

    @classmethod
    def load_creatures(cls):
        creatures = [Character("Dragon",10,22),
                     Character("Orc",7,10),
                     Character("Skeleton",5,8),
                     Character("Large rat",6,6),
                     ]
        return creatures

    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures

    def choose_opponent(self):
        self.opponent = Character("Extremely large rat",10,6)
        #self.opponent = random.choice(self.creatures)
        #self.creatures.remove(self.opponent)

    def set_player(self, player_character):
        self.player = player_character

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def return_characters_status(self):
        msg = (self.player.return_character_status()+'\n'+self.opponent.return_character_status())
        return msg

    def return_round_result(self,other):
        if self.player.fight_round(other) == 'won':
            return f"{self.player.return_roll_status()}\n{self.opponent.return_roll_status()}\n{self.player.name} won this round"
        elif self.player.fight_round(other) == 'lost':
            return f"{self.player.return_roll_status()}\n{self.opponent.return_roll_status()}\n{self.player.name} lost this round"
        else:
            return f"{self.player.return_roll_status()}\n{self.opponent.return_roll_status()}\n{self.player.name} and {self.opponent.name} drew this round"

class GameCLI:

    def __init__(self):
        self.game = Game()
        self.run_game()

    def run_game(self):
        print("Welcome to Fighting Fantasy!")
        player_name = input("What is your name? ")
        self.game.set_player(PlayerCharacter.generate_player_character(player_name))
        print(f"Welcome {player_name}!")
        print(self.game.player.return_character_status())
        self.fight_opponent()

    def fight_opponent(self):
        self.game.choose_opponent()
        print(f"You will be fighting {self.game.opponent.name}!")
        print(self.game.opponent.return_character_status() + '\n')
        self.fight_battle()

    def fight_battle(self):
        continue_battle = True
        while continue_battle:
            print(self.game.return_characters_status())
            print()
            action = input("Would you like to fight a round (y/n)? ").strip().lower()
            if action == 'n':
                print("You flee in terror!")
                continue_battle = False
            else:
                self.game.resolve_fight_round()
                print(self.game.return_round_result(self.game.opponent))
                if self.game.player.is_dead:
                    print("You died")
                    continue_battle = False
                if self.game.opponent.is_dead:
                    print(f"You defeated the {self.game.opponent.name}")
                    continue_battle = False

if __name__ == '__main__':
    GameCLI()

