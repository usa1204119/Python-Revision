def get_formatted_name(first,last,middle=''):
    """ Return a fully formatted name """
    if middle:
         full_name = first + ' ' + middle + ' ' +  last
    else:
        full_name = first + ' ' + last
    return full_name.title()
name = get_formatted_name('Utkarsh','Sharma','Anurag')
print(name)

# returning a dictionary
def build_name(first,last,age=''):
    person = {'first_name': first , 'last_name':last}
    if age:
        person['age'] = age
    return person
person = build_name('Utkarsh','Sharma',age=17)
print(person)

# using a function with a while loop
def get_formatted_name(first,last):
    full_name = first + ' ' + last
    return full_name.title()
# this is an infinite loop
print('Enter q to end the program.')
while True:
    f_name = input('first name : ')
    if f_name == 'q':
        break
    l_name = input('last name : ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(formatted_name)


