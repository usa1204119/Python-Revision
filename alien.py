alien = {'colour':'green','points':5}
print(alien['colour'])
print(alien['points'])

# Accessing values in dictionary
new_points = alien['points']
print('You just earned ' + str(new_points) + ' points.')

# Adding new key value pair
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# starting with new dictionary
alien = {}
alien['colour'] = 'green'
alien['points'] = 5
print(alien)

# modifying values in dictionary
print('The alien colour is ' + alien['colour'] + '.')
alien['colour'] = 'yellow'
print('The alien colour is  now ' + alien['colour'] + '.')

alien = {'x_position':0,'y_position':25,'speed':'medium'}
# defining the original position
print('Original_position : ' + str(alien['x_position']))
# move the alien to right
# determine how far is the alien is based on the current speed
if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	# this must be a fast alien
	x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print('New position : ' + str(alien['x_position']))

# deleting key value pair
del alien['x_position']
print(alien)

alien_0 = {'colour':'green','points':5,'speed':'slow'}
alien_1 = {'colour':'yellow','points':10,'speed':'slow'}
alien_2 = {'colour':'red','points':15,'speed':'slow'}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

aliens = []
for alien in range(300):
	new_alien =  {'colour':'yellow','points':15,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['colour'] == 'yellow':
		alien['colour'] = 'purple'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['colour'] == 'green':
		alien['colour'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)
print('...')
print(len(aliens))

# store info about a  pizza being ordered
pizza = {
	'crust':'thick',
	'toppings':['mushroom','pepperoni'],
	}
print('I want a pizza with ' + pizza['crust'] + ' crust with the following toppings : ')
for topping in pizza['toppings']:
	print('\t'+ topping)

favourite_language = {
	'Shivam':['Python','Java'],
	'Utkarsh':['Python','R'],
	'Robin':['C','C++'],
	'Abusad':['Javascript','html'],
	}

for name,languages in favourite_language.items():
	print(name.title() + "'s favourite languages are : ")
	for language in languages:
		print('\t'+ language)

users = {
	'aeinstein': {
	'first_name':'Albert',
	'last_name':'Einstein',
	'location':'Princeton',
	},
	'mcurie':{
	'first_name':'Marie',
	'last_name':'Curie',
	'location':'Paris',
	},
	}

for username,user_info in users.items():
	print('Username : ' + username )
	full_name = user_info['first_name'] + user_info['last_name']
	location = user_info['location']

	print('\tFull Name : '+full_name.title())
	print('\tLocation : ' + location )


person = []
person_1 = {
	'name':'Utkarsh Sharma',
	'age':17,
	'city':'Boisar'
}
person.append(person_1)
person_2 = {
	'name':'Gaurav Singh',
	'age':19,
	'city':'Boisar'
}

person.append(person_2)
person_3 = {
	'name':'Shivam Yadav',
	'age':17,
	'city':'Boisar'
}
person.append(person_3)

for person in person:
	name = person['name']
	age = person['age']
	city = person['city']
	print(name.title() + ' of ' + city + ' is ' + str(age) + ' years old.')

pets = []
pet = {
	'animal_type':'python',
	'pet_name':'john',
	'weight':43,
	'eats':'bugs',
	}
pets.append(pet)
pet = {
	'animal_type':'cat',
	'pet_name':'meowth',
	'weight':5,
	'eats':'',
	}
pets.append(pet)
pet = {
	'animal_type':'python',
	'pet_name':'john',
	'weight':43,
	'eats':'bugs',
	}
pets.append(pet)

for pet in pets:
	print('Here is what I know about ' + pet['pet_name'].title() + ':')
	for k,v in pet.items():
		print('\t' + k + ':' + str(v))


favourite_places = {
	'Shivam':['California','LasVegas','Dubai'],
	'Utkarsh':['Paris','DisneyLand','Agra'],
	'Vishnu':['Thailand','Alahabad','Benaras'],
	}
for name,places in favourite_places.items():
	print(name.title() + "'s favourite places are : ")
	for place in places:
		print('\t'+place.title())

cities = {
	'Delhi':{
		'country':'India',
		'popultaion':20000000,
		'fact':'Capital of India'},
	'Mumbai':{
		'country':'India',
		'popultaion':12500000,
		'fact':' film industry',
	}
	}
for city,city_info in cities.items():
	country = city_info['country']
	population = city_info['popultaion']
	fact = city_info['fact']

	print('\n'+city.title() + ' is in ' + country)
	print('It has a popultaion of ' + str(population))
	print('It is famous as '+fact)

	