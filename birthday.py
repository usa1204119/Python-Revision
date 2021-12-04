file_name = 'pi_million_digits.txt'
with open(file_name) as f_obj:
    lines = f_obj.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
birthday = input('Enter your birthday to check weather it appears in million digits of pi !'
                + ' Enter in MM/DD/YY format')
if birthday in pi_string:
    print('Your birthday appears in million digits of pi!')
else:
    print('Your birthday does not appears in the first million digits of pi.')