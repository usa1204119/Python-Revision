from random import randint
class Die():
    """ A simple attempt to model a die """
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        """ Return a number between 1 and number of sides """
        return randint(1,self.sides)
    
d6 = Die()
results = []
for roll in range(10):
    result = d6.roll_die()
    results.append(result)
from random import randint
class Die():
    """ A simple attempt to model a die """
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

# make a die of 6 sides and roll it over 10 times   
d6 = Die()
results = []
for roll in range(10):
    result = d6.roll_die()
    results.append(result)
print('The 10 roll of 6 sided dies : ')
print(results)

# make a die of 10 sides and roll it over 10 times
d10 = Die(sides=10)
results = []
for roll in range(10):
    result = d10.roll_die()
    results.append(result)
print('The 10 roll of 10 sided dies : ')
print(results)

# make a die of 20 sides and roll it over 10 times
d20 = Die(sides=20)
results = []
for roll in range(10):
    result = d20.roll_die()
    results.append(result)
print('The 10 roll of 20 sided dies : ')
print(results)
