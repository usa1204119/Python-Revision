# creating a class dog
class Dog():
	"""  Attempt to model a simple dog """
	def __init__(self,name,age):
		self.name = name 
		self.age = age 

	def sit(self):
		print(self.name.title() + ' is sitting now.')
	def roll(self):
		print(self.name.title() + ' just rolled over.')
dog = Dog('Tuffy',10)
print('My dog name is ' + dog.name.title())
print('My dog is ' + str(dog.age) + ' years old.')
dog.sit()
dog.roll()
dog = Dog('Drake',5)
print('My dog name is ' + dog.name.title())
print('My dog is ' + str(dog.age) + ' years old.')
dog.sit()
dog.roll()
