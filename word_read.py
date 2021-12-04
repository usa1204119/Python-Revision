def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print('The file '+ filename + ' does not exist.')
    else:
        # count the total number of words file has
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has total ' + str(num_words) + ' number of words.')
filenames = ['alice.txt','siddharta.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)