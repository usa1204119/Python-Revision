from privileges import *
utkarsh = Admin('Shivam','Yadav','syadav','Boisar','syadav@gmail.com')
utkarsh.describe_user()
utkarsh_privileges = ['can edit post','can remove user','can ban user']
utkarsh.privileges.privileges = utkarsh_privileges
utkarsh.privileges.show_privileges()