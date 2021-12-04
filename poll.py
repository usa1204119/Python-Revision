file_name = 'programming_poll.txt'
responses = []
while True:
    response = input('Why do you like programming ? ')
    responses.append(response)
    continue_poll = input('Would you like anyone else to poll (y/n)')
    if continue_poll == 'n':
        break
with open(file_name,'a') as f:
    for response in responses:
        f.write(response + '\n')