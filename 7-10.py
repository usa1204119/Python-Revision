dream_vacation = {}
active = True
while active:
    name = input('What is your name ? ')
    vacation = input('What is the dream place you would like to visit ?')
    dream_vacation[name] = vacation

    repeat = input('Would you like to mention some other name(yes/no)')
    if repeat == 'no':
        active = False

for name,vacation in dream_vacation.items():
    print(name.title() + ' would like to visit ' + vacation + ' once in his lifetime.')