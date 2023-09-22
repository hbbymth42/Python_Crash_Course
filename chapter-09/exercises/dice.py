from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

dice = Die()
for i in range(10):
    dice.roll_die()

dice.sides = 10
for i in range(10):
    dice.roll_die()

dice.sides = 20
for i in range(10):
    dice.roll_die()