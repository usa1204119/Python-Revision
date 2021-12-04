print('Enter quit to end the program')
while True:
    try:
        x = input('first_number : ')
        if x == 'quit':
            break
        x = int(x)
        y = input('Second_number : ')
        if y == 'quit':
            break
        y = int(y)
    except ValueError:
        print('Sorry I really need a number.')
    else:
        sum = x + y
        print('The sum of two numbers are ' + str(sum))
