favourite_language = {
	'Shivam':'Java',
	'Utkarsh':'python',
	'Abusad':'C++',
	'Robin':'C',
	'Gaurav':'C'
	}

print("Utkarsh's favourite language is " + favourite_language['Utkarsh'].title() + '.')

person = {
	'first_name':'Utkarsh',
	'last_name':'Sharma',
	'city':'Boisar',
	'age':17,
	}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

favourite_numbers = {
	'Shivam':1,
	'Utkarsh':2,
	'Gaurav':3,
	}
num = favourite_numbers['Shivam']
print("Shivam's favourite number is " + str(num) + '.' )
num = favourite_numbers['Utkarsh']
print("Utkarsh's favourite number is " + str(num) + '.' )
num = favourite_numbers['Gaurav']
print("Gaurav's favourite number is " + str(num) + '.' )

programming_words = {
	'string':'Set of characters.',
	'comments':'A note that is ignored.',
	'list':'A collection of items in a particular order.',
	'loop':'work through a collection of items once at a time.',
	'tuple':'A collection of items that are immutable.',
	'dictionary':'A collection of key value pairs.',
	'bollean':'A value which is either True or False.',

	}
words = 'string'
print('\n' + words.title() + ':')
print(programming_words['string'])
words = 'comments'
print('\n' + words.title() + ':')
print(programming_words['comments'])
words = 'comments'
print('\n' + words.title() + ':')
print(programming_words['comments'])
words = 'list'
print('\n' + words.title() + ':')
print(programming_words['list'])
words = 'loop'
print('\n' + words.title() + ':')
print(programming_words['loop'])

# loopig through all k,v pairs in dictionary
for k,v  in programming_words.items():
	print('\n' + k+':' + '\n' + v)

for k,v in programming_words.items():
	print('Key : ' + k)
	print('Value :' + v)

for name,language in favourite_language.items():
	print(name.title() + "'s favourite language is " + language.title())
friends = ['Shivam','Abusad']
for name in favourite_language.keys():
	if name in friends:
		print(name.title() + ', I see your favourite language is ' + favourite_language[name].title())
if 'Gaurav' not in favourite_language:
	print('Gaurav please take your poll')

# looping through a dictionary keys in order
for name in sorted(favourite_language.keys()):
	print(name.title() + ', thankyou for taking the poll.')
	
print('The following languages have been mentioned')
for language in set(favourite_language.values()):
	print(language.title())

rivers = {'Ganga':'India','Amazon':'Brazil','Nile':'Africa'}
for river,country in rivers.items():
	print(river.title() + ' runs through ' + country.title() + '.')

for name,language in favourite_language.items():
	print(name.title() + "'s favourite language is " + language.title())
friends = ['Utkarsh','Abusad','Abhishekh','Afrahim']
for friend in friends:
	if friend in favourite_language.keys():
		print('Thanks for taking the poll ' + friend.title())
	else:
		print('Please take the poll ' + friend.title())