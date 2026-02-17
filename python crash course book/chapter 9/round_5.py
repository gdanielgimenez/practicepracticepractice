# 9-14 Orderect Dict start with excercise 6.4 glossary
from dices import Die
from collections import OrderedDict

glossary = OrderedDict()

glossary = {'Boolean': 'a value that can be only True or False',
            'Python': 'a Dynamically typed language',
            'function': 'a block of code that runs when its called',
            }
# for key, item in glossary.items():
#    print(f"\n{key} : {item}")

# 6.4 Glossary 2 adding new values to 6.3
glossary['int'] = "integer number values"
glossary['float'] = "float number values"
glossary['import'] = "Keyword used to import modules"

for key, item in glossary.items():
    print(f"\n{key} : {item}")

# 9.14 Dice class will be in a separate file

six_side_die = Die()
# loop to call the funct to roll the die x number of times
for _ in range(1, 7):
    six_side_die.roll_die()

print()

ten_side_die = Die(10)
# loop to call the funct to roll the die x number of times
for _ in range(1, 11):
    ten_side_die.roll_die()

print()
twenty_side_die = Die(20)
# loop to call the funct to roll the die x number of times
for _ in range(1, 21):
    twenty_side_die.roll_die()
