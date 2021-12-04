def pet(animal_type,animal_name):
    print('I have a '+ animal_type + '.')
    print('My '+ animal_type + "'s name is " + animal_name.title() + '.')

# positional argument
pet('cat','meowth')
# multiple function call
pet('dog','Drake')
#  order matters in positional arguments
pet('harry','hamster')
# keyword arguments
pet(animal_name='harry',animal_type='hamster')

# Default value
def pet(animal_name,animal_type='dog'):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + animal_name.title() + '.')
pet('Drake')
pet('Moti')
# overwriting the default value
pet(animal_name='bella',animal_type='cat')
