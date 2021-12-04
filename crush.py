crushes = {}
active = True
while active:
    name = input('What is your name ?')
    crush = input('Who is your crush ?')
    crushes[name] = crush
    repeat = input('Would you like to mention someone else name ? ')
    if repeat == 'no':
        active = False
print('\n----The polling results are ----')
for name,crush in crushes.items():
    print(name.title() +' would like to marry ' + crush + ' one day.')