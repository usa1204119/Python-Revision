try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide a number by zero.')

print('Give me two number and I will divide them!')
print('Enter quit to end the program.')
while True:
    first_number = input('First_number')
    if first_number == 'quit':
        break
    second_number = input('Second_number')
    if second_number == 'quit':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide a number by zero!')
    else:
        print(answer)