import json
username = input('What is your name ? ')
file_name = 'username.json'
with open(file_name,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you will come back .")
