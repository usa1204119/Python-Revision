# removing alll instances of a specific value from a list
pets = ['dog','cat','cat','cow','hamster','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# filling a dictionary with user input
# create a dictionary to hold the responses
responses = {}
# set a flag stating that the polling active is true
polling_active = True
while polling_active:
	# prompt the user to input his name and name of the mountain he would like to climb 
	name = input('What is your name ? ')
	response = input('Which mountain would you like to climb one day ?')
	# store the responses in a dictionary
	responses[name] = response

	# ask the users if anyone else is going to poll
	repeat = input('Is anyone else going to poll(yes/no)')
	if repeat == 'no':
		polling_active = False

print('\n---The polling results are ---')
for name,response in responses.items():
	print(name.title() + ' would like to climbe ' + response + ' one day.')