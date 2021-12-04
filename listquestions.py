names = ['Utkarsh','Shivam','Vishnu','Robin']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print('Hello, ' + names[1])
print('Hello, ' + names[2])
print('Hello, ' + names[3])

transportation = ['car','aeroplane','boat','railway']
print('I would like to travel by ' + transportation[-2] + ' one day. ')

# invitation to people
guests = ['Shivam','Robin','Vishnu','Rohit']
for guest in guests:
	print(guest + ' it would be great if you attend dinner session tonight.')

print('Rohit cant make it tonight.')
guests[-1] = 'Afrahim'
print(guests)
for guest in guests:
	print(guest + ' you are highly invited to dinner session tonight.')
print('Hey,dudes I just found a big dinner table' 
	+' so couple more friends would be joining us.')

guests.insert(0,'Abhishekh')
guests.insert(3,'Gaurav')
guests.append('Deepak')
print(guests)
for guest in guests:
	print(guest + ' you have been invited to dinner session tonight.')
print('Its a great sorry as I could be able to arrange big dinner table tonight .')
print(guests)
print('Sorry ' + guests.pop(0))
print('Sorry ' + guests.pop(1))
print('Sorry ' + guests.pop(1))
print('Sorry ' + guests.pop(2))
print('Sorry ' + guests.pop(2))

print(guests)
for guest in guests:
	print(guest + ' I highly welcome you to attend dinner session tonight.')

# seeing the world
places = ['California','LasVegas','Agra','Paris','London']

print('\nOriginal order : ')
print(places)

print('\nSorted order')
print(sorted(places))

print('\nOriginal order :')
print(places)

print('\nSorted reverse order : ')
print(sorted(places,reverse=True))

print('\nOriginal order : ')
print(places)

print('\nReverse order :')
places.reverse()
print(places)

print('\nOriginal order: ')
print(places)

print('\nSorted list : ')
places.sort()
print(places)

print('\nOriginal order')
print(places)

print('\nReverse order : ')
places.sort(reverse=True)
print(places)

print('\nOriginal Order : ')
print(places)

# dinner guest 
print('\nGuest Invited : ')
print(str(len(guests)) + ' guests are invited to join the dinner session tonight.')


# every function
print('\n')
countries = ['India','America','Russia','France','Japan']

print('\nTemperory sorting : ')
print(sorted(countries))
print(countries)

print('\nPermenant sort')
countries.sort()
print(countries)

print('\nreverse')
countries.sort(reverse = True)
print(countries)

print('\nRemove')
countries.remove('Russia')
print(countries)

print('\nAdding elements in last : ')
countries.append('Russia')
print(countries)

print('\nAccessing elements : ')
print(countries[0].upper())

print('\nWriting message : ')
print('I love my ' + countries[1].title() + '.')

print('\nChanging elements')
countries[2] = 'Australia'
print(countries)

print('\nAdding elements anywhere : ')
countries.insert(3,'Russia')
print(countries)

print('\nRevmoving elements : ')
del countries[2]
print(countries)

print('\nRemoving elements using pop :')
countries.pop(-1)
print(countries)

print('\nRemoving items by value : ')
countries.remove('Russia')
print(countries)

print('\nLength of list')
print(len(countries))