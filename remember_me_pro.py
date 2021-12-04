import json
def greet_user():
    """ greet the user by name """
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name : ')
        with open(file_name,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back.")
    else:
        print('Welcome, '+ username)    
greet_user()