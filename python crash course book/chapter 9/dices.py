from random import randint


class Die():
    """attemp model for dices"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rolled = randint(1, self.sides)
        print(f"You rolled : {rolled}")
