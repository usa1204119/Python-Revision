import json
file_name = 'fav_number.json'
try:
    with open(file_name) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    fav_num = input('Which is your favourite number ? ')
    with open(file_name,'w') as f_obj:
        json.dump(fav_num,f_obj)
        print("Thanks,I'll remember that.")
else:
    print('I know your favourite number is ' + str(fav_num))