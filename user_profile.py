def build_user(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
user = build_user('Utkarsh','Sharma',location='Boisar',field='Science')
print(user)

def make_sandwich(*items):
	print('\nI will make your sandwich a great sandwich : ')
	for item in items:
		print('Adding ' + item)
	print('Finished making your sandwich!')
order = make_sandwich('roast_beef','cheedar','lettuce')
order1 = make_sandwich('peanut_butter','strawberry_jam')

# cars
def car(name,model,**additional_features):
	cars = {}
	cars['name'] = name 
	cars['model'] = model 
	for key,value in additional_features.items():
		cars[key] = value
	return cars
car = car('Scorpio','8 sitter',colour='Black',sound='8d audio system')
print(car)
