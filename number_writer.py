import json
numbers = [2,3,4,5,5,6,6,5,65,6,44]
file_name = 'numbers.json'
with open(file_name,'w') as f_obj:
    json.dump(numbers,f_obj)
    