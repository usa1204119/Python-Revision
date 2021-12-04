# Alien colour #1
alien_colour = 'green'
if alien_colour == 'green':
	print('You just earned 5 points.')
alien_colour = 'red'
if alien_colour == 'green':
	print('You just earned 5 points.')

# alien colour #2
alien_colour = 'red'
if alien_colour == 'red':
	print('You just earned 5 points.')
else:
	print('You just earned 10 points.')


alien_colour = 'red'
if alien_colour == 'yellow':
	print('You just earned 5 points.')
elif alien_colour == 'red':
	print('You just earned 10 points.')
else :
	print('You just earned 15 points.')

age = 56
if age < 2 : 
	print('The person is a baby.')
elif age < 4:
	print('The person is a toddler.')
elif age < 13:
	print('The person is a kid.')
elif age < 20:
	print('The person is a teenager.')
elif age < 65:
	print('The person is an adult.')
else:
	print('The person is an elder.')

favourite_fruit = ['apple','banana','lime']
if 'apple' in favourite_fruit:
	print('You really like apple.')
if 'banana' in favourite_fruit:
	print('You really like banana.')
if 'lime' in favourite_fruit:
	print('You really like lime.')
if 'chikoo' in favourite_fruit:
	print('You really like chikoo.')

users = []
if users:
	for user in users:
		if user == 'Admin Abusad':
			print('Hello ' + user + ' would you like to see status report.')
		else:
			print('Hello ,' + user + ' thankyou for logging in .')
else:
	print('We need to find some users!')

current_usernames = ['utkarsh','shivam','robin','abusad']
new_usernames = ['abhishekh','afrahim','shivam','utkarsh']
for new_username in new_usernames:
	if new_username in current_usernames:
		print('This username is not available.') 
	else:
		print('This username is available.')

numbers = list(range(1,11))
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(str(number) + 'th')

