file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry the file ' + file_name + ' does not exist.'
    print(msg)
else:
    # count the total number of words in the file
    words = contents.split()
    num_words = len(words)
    print('The file ' + file_name + ' has total ' + str(num_words) + ' number of words.') 

