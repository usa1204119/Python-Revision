file_name = 'pi_million_digits.txt'
with open(file_name) as f_obj:
    lines = f_obj.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:52] + '...')
print(len(pi_string))