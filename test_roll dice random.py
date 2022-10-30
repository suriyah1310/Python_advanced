#create class called dice
#create a method roll in dice
#get tuple of two random values
import random
import tuples

class Dice:
    def roll():
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        olist = (x, y)
        print(tuple(olist))

Dice.roll()





