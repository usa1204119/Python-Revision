guest_name = input('What is your name : ')
file_name = 'guest.txt'
with open(file_name,'a') as f_obj:
    f_obj.write(guest_name.strip())