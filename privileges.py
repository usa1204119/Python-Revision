class User():
	def __init__(self,first,last,username,location,email):
		self.first = first.title()
		self.last = last.title()
		self.username = username
		self.location = location
		self.email = email
		self.login_attempts = 0
	def describe_user(self):
		print(self.first + ' ' + self.last)
		print(' Username : ' + self.username)
		print(' Location :' + self.location)
		print(' Email ID : ' + self.email)

	def greet_user(self):
		print('Hello , ' + username)

	def login_attempt(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges:
            print('\nPrivileges : ')
            for privilege in self.privileges:
                print('-' + privilege)
        else:
            print('This user has no privileges .')
class Admin(User):
    def __init__(self, first, last, username, location, email):
        super().__init__(first, last, username, location, email)
        self.privileges = Privileges()
