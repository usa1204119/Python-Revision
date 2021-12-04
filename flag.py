prompt = 'Tell me something and I will repeat it back : '
prompt += 'Enter quit to end the program '

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

