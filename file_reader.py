# reading file line by line
file_name = 'pidigits.txt'
with open(file_name) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    print(line.rstrip())