prompt = 'What is your age ?'
prompt += 'Enter quit to end the program'
while True:
	message = input(prompt)
	if message != 'quit':
		break
	message = int(message)
	if message < 3 :
		print('The ticket is free.')
	elif message < 12:
		print('The ticket price is 10$.')
	else:
		print('The ticket price is 15$.')

