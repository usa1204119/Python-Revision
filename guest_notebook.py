file_name = 'guest.txt'
print('Enter quit when you are finished.')
while True:
    name = input('What is your name ?')
    if name == 'quit':
        break
    else:
        with open(file_name,'a') as f_obj:
            f_obj.write(name+'\n')
        print('Hi, ' + name + ' you have been added to guest book.')