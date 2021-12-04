# if value in list then perform the following tasks 
cars = ['audi','bmw','lamborghini','Ferrari']
for car in cars : 
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# checking the values in list
requested_toppings ='mushroom'
if requested_toppings != 'anchovies':
	print('Hold the anchovies!')
print('mushroom' in requested_toppings)
print('mushoom' in requested_toppings)

banned_users = ['Utkarsh','Shivam','Robin']
users = 'Gaurav'
if users not in banned_users:
	print(users.title() + ', you can post a response if you wish.')

car = 'audi'
print("Is car == 'audi' I predict ture")
print(car=='audi')
print("Is car == 'bmw' I predict false")
print(car == 'bmw')

age = 56
print(age<45)
print(age==45)
print(age!=45)
print(age>45)
print(age<=45)

age = 19
if age >= 18:
	print('You are old enough to vote!')
	print('Have you registered to vote yet!')
else:
	print('You are not eligible to vote')
	print('Get yourself registered as soon as you turn 18.')

age = 199
if age < 4:
	price = 0
elif age < 12:
	price = 5
elif age > 65:
	price = 5
else:
	price = 10

print('Your admission fees is ' + str(price) + '$.')

requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
	print('Adding mushroom')
elif 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
	print('Adding extra cheese')
print('\nFinished making your pizza.')

