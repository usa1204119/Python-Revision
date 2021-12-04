# writing to a file
with open('writing_text.txt','a') as f_obj:
    f_obj.write('I love programming.\n')
    # writing multiple lines
    f_obj.write('I love creating new games.\n')
    f_obj.write('I love creating apps that run on browsers.\n')
    f_obj.write('I love finding finding meaning on large data sets.')