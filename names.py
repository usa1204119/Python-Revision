from name_function import get_formatted_name
print('Enter quit to end the program')
while True:
    first = input('What is your first name : ')
    if first == 'quit':
        break
    last = input('What is your last name : ')
    if last == 'quit':
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)