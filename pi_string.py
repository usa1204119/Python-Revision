# working with file contents
file_name = 'pidigits.txt'
with open(file_name) as f_obj:
    lines = f_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

