file_name = 'learning_python.txt'
# reading over entire file
with open(file_name) as f_obj:
    contents = f_obj.read()
    print(contents)

# reading over line by line in a file
print('\n')
with open(file_name) as f_obj:
    for line in f_obj:
        print(line.rstrip())
print('\n')

# reading by making a list
with open(file_name) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.rstrip())

    