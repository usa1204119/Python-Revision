# replace 
message = 'I really like dog'
print(message.replace('dog', 'cat'))

file_name = 'learning_python.txt'
with open(file_name) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    print(line.rstrip().replace('python','C'))