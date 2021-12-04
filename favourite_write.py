import json
favourite_number = input('Which is your favourite number ?')
file_name = 'fav_number.json'
with open(file_name,'w') as f_obj:
    json.dump(favourite_number,f_obj)
    print("Thanks,I'll remember that.")