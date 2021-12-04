def make_pizza(size,*toppings):
	""" Describe the pizza your are about to make """
	print('I want a pizza of ' + str(size) + ' inches with the following toppings : ')
	for topping in toppings:
		print('-'+ topping)
make_pizza(16,'mushroom','pepperoni')

