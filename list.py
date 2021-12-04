bicycles = ['trek','avon','Bsa','speed']
print(bicycles)
print(bicycles[0].title())
print(bicycles[2].upper())
print(bicycles[1].lower())
print(bicycles[-1].title())
message = 'My first bicycle was ' + bicycles[2].title()
print(message)

# modifying elements in a list
names = ['Utkarsh','Shivam','Vishnu','Robin']
names[0] = 'Abhishekh'
print(names)

# Adding elements in a list
names.append('Utkarsh')
print(names)

# Appending elements to the last of list
motorcycles = []
motorcycles.append('Hayabusa')
motorcycles.append('KTM')
motorcycles.append('Kawasaki Ninja')

print(motorcycles)

# Inserting elements into the list

motorcycles.insert(0,'ducati')
print(motorcycles)

# removing values by order
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

names = ['Utkarsh','Shivam','Vishnu','Robin']
names.remove('Utkarsh')
print(names)


# removing item by value
bicycles = ['trek','avon','Bsa','speed']
too_expensive = 'trek'
bicycles.remove(too_expensive)
print('A ' + too_expensive + ' is too expensive for me.')

# organizing a list
cars = ['Honda','Lamborghini','Audi','Ferrari']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


# Sustaining the original list
cars = ['Honda','Lamborghini','Audi','Ferrari']

print('\nHere is the original list : ')
print(cars)
print('\nHere is the sorted list : ')
print(sorted(cars))
print('\nHere is the oringinal list again : ')
print(cars)

cars.reverse()
print(cars)
print(len(cars))


countries = []
print(countries)