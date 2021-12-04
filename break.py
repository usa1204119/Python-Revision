prompt = 'Please enter the name of city you would like to visit.'
prompt += 'Enter quit to end the program '

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print('I would like like to visit ' + message.title() + ' one day.')