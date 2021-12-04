# start with the users that needs to be verified
# add the users to new list of confirmed users
unconfirmed_user = ['Utkarsh','Shivam','Robin','Gaurav','Vishnu','Abhishekh']
confirmed_user = []
while unconfirmed_user:
	current_user = unconfirmed_user.pop()
	print('Verifying users : '+ current_user)
	confirmed_user.append(current_user)
print('The following users have been confirmed : ')
for confirmed_user in confirmed_user:
	print(confirmed_user)