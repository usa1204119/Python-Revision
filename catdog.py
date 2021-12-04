file_names = ['cat.txt','dog.txt']
for file_name in file_names:
    print('Reading Files : ' + file_name)
    try:
        with open(file_name) as f:
            contents = f.read()
            print(contents)
    # silent cat dogs
    except FileNotFoundError:
        pass