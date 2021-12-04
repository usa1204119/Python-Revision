# passing a list
def greet_user(names):
    for name in names:
        print('Hello, ' + name)
usernames = ['Utkarsh','Shivam','Robin','Abhishekh','Vishnu','Gaurav']
greet_user(usernames)

# printing models
def print_models(unprinted_models,completed_models):
    while unprinted_models:
        current_models =  unprinted_models.pop()
        print('Printing models : ' + current_models)
        completed_models.append(current_models)
def show_completed_models(completed_models):
    print('The following models have been printed : ')
    for completed_model in completed_models:
        print(completed_model)

unprinted_models = ['Iphone Case','Wardrobe design','Ceramic Tiles']
completed_models = []

print_models(unprinted_models[:],completed_models)
show_completed_models(completed_models)
print(unprinted_models)