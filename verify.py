import json
def get_stored_username():
    """ Check weather the name is stored"""
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input('What is your name? ')
    file_name = 'username.json'
    with open(file_name,'w') as f:
        json.dump(username,f)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        correct = input('Are you ' + username +  ' ?(y/n) ')
        if correct == 'y':
            print('Welcome, ' +   username)
        else:
            username = get_new_username()
            print("We'll remember when you will comeback")

    else:
        username = get_new_username()
        print("We'll remember when you will comeback")
greet_user()
