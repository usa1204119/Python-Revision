current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = 'Tell me something and I will repeat it back : '
prompt += 'Enter quit to end the program '

message = ''
while message != 'quit':
	message = input(prompt)
if message != 'quit':
        print(message)

#  using a flag