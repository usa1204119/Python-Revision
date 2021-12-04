from car import Car,ElectricCar # importing multiple classes in module
car = ElectricCar('Nissan','Duet',2020)
car.battery.describe_battery()
car.battery.get_range()
car.describe_car()
cars = Car('Tata','Nano',2016)
cars.describe_car()
from car import * # import all class in module
cars = Car('Tata','Nno',2016)
cars.describe_car()
