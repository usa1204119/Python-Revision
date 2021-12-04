class Resturant():
	""" A simple attempt to model a resturant """
	def __init__(self,name,cuisine_type):
		self.name = name 
		self.cuisine_type = cuisine_type

	def describe_resturant(self):
		print(self.name.title() + ' serves the best ' + self.cuisine_type + ' food in our area.')

	def open_resturant(self):
		print(self.name.title() + ' is open now.')


class IcecreamStand(Resturant):
	def __init__(self,name,cuisine_type):
		super().__init__(name,cuisine_type)

	def show_flavours(self):
		print('We have the following flavours : ')
		for flavour in self.flavours:
			print(flavour)

utkarsh = IcecreamStand('Utkarsh Shahi Dawaat','Indian Style')
utkarsh.flavours = ['Vanilla','Chocolate','Strawberry']

utkarsh.describe_resturant()
utkarsh.show_flavours()