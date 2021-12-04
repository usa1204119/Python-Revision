# creating a class
class Car():
	""" A simple attempt to model a car """
	def __init__(self,make,model,year): # defining a self 
		self.make = make # defining a name and other values
		self.model = model 
		self.year = year
		self.odometer_reading = 0 # defining default value

	def describe_car(self): # making a function called describe car
		print(self.make + ' ' +  self.model + ' ' +  str(self.year))
	def reading(self):
		print('This car has ' + str(self.odometer_reading) + ' miles on it .')

	# updating a default value via method
	def update_odometer(self,milage):
		self.odometer_reading = milage

	# incrementing the odometer value via method
	def increment_odometer(self,miles):
		self.odometer_reading += miles

car = Car('Tesla','Phantom',2021) # calling a class
# defining a battery class
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
	def describe_battery(self):
		print('This car has '+ str(self.battery_size) + '-kwh battery.')
	def get_range(self):
		if self.battery_size == 70:
			range = 210
		elif self.battery_size == 85:
			range = 260
		message = 'This car can go ' + str(range) + ' miles on full charge.'
		print(message)
	def upgrade_battery(self):
		if self.battery_size == 70:
			self.battery_size = 85
			print('Your battery is upgraded')
		else:
			print('You cant roll back the odometer.')
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()
		