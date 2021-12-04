import json
def get_stored_username():
    """ Get stored username if available """
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input('What is your name ?')
    file_name = 'username.json'
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """ greet the user by name """
    username = get_stored_username()
    if username:
        print('Welcome, ' + username)
    else:
        username = get_new_username()
        print("We'll remember you when you will come back.")
greet_user()
