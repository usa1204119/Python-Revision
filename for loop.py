magicians = ['alice','david','caroline']
for magician in magicians:
	print(magician.title() + ', that was a great trick!')
	print('I cant wait to see next trick ' + magician.title() + '.' + '\n' )
print('Thankyou everyone, That was a great magic show!')

print('\n')
pizzas = ['cheese','pepperoni','mushroom']
for pizza in pizzas:
	print(pizza + ' pizza is my favourite.')
print('I really like pizza!')


animals = ['dog','cat','cow']
for animal in animals:
	print('A ' + animal + ' would make a great pet.')
	print(animal + ' is very caring.')

# range
for value in range(1,10):
	print(value)
# even numbers
for value in range(0,20,2):
	print(value)
# odd numbers
for value in range(1,20,2):
	print(value)
squares=[value**2 for value in range(1,11)]
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))


# counting to 20
for value in range(1,21):
	print(value)

# odd number from 1 to 20
for value in range(1,21,2):
	print(value)
# even number from 1 to 20
for value in range(0,21,2):
	print(value)

# multiples of 3
for value in range(3,31,3):
	print(value)

cubes = [value**3 for value in range(1,11)]
print(cubes)
print(max(cubes))
print(min(cubes))
print(sum(cubes))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[3:])
for player in players[:3]:
	print(player)

my_foods = ['Fried Rice','Chicken','Paneer']
my_friends_food = my_foods[:]
print('My favourite foods are :')
print(my_foods)
print('My friends favourite foods are :')
print(my_friends_food)
my_foods.append('Rajma Chawal')
my_friends_food.append('Ice Cream')
print(my_foods)
print(my_friends_food)
print('\nThe list of my foods are :')
for food in my_foods:
	print(food)
print('\nThe list of my friends foods are :')

for food in my_friends_food:
	print(food)
pizzas = ['cheese','pepperoni','mushroom','pineapple','olive']
print('The three toppings are : ')
for pizza in pizzas[:3]:
	print(pizza)

print('The middle three toppings are : ')
for pizza in pizzas[1:4]:
	print(pizza)
print('The last three items in the list are : ')
for pizza in pizzas[2:]:
	print(pizza)
