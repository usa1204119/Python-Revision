requested_toppings = ['mushroom','pepperoni','extra cheese']
for toppings in requested_toppings:
	if toppings == 'pepperoni':
		print('Sorry, we are out of pepperoni.')
	else:
		print('Adding ' + toppings + '.')
print('\nFinished making your pizza.')

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding ' + requested_topping)
	print('\nFinished making your pizza.')
else:
	print('Are you sure you want plain pizza.')

available_toppings = ['mushroom','pepperoni','extra cheese'
                       'olive','green peppers','pineapple']
requested_toppings = ['mushroom','french fries','green peppers']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding '+ requested_topping)
	else:
		print('Sorry, we dont have ' + requested_topping)
	print('\nFinished making your pizza.')

	