from privileges import Admin
user = Admin('Utkarsh','Sharma','usharma','Boisar','utkarsh1204119@gmail.com')
user.describe_user()
user_privileges = ['can edit post']
user.privileges.privileges = user_privileges
user.privileges.show_privileges()