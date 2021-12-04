# passing arbitary number of arguments in a function
# making positional and arbitary arguments
def make_pizza(size,*toppings):
    print('Make a ' + str(size) + ' inches pizza with the following toppings : ')
    for topping in toppings:
        print(topping)
    
make_pizza(15,'pepperoni','extra cheese')
make_pizza(12,'mushroom')

def build_person(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user = build_person('Utkarsh', 'Sharma',location='Boiasr',field='Science')
print(user)