#Vehicle class
class Vehicle(object):
	def __init__(self,engine_type,**kwargs):
		for key,value in kwargs.items():
			setattr(self,key,value)

	def set_color(self):
		pass
	def set_color(self):
		pass



class Car(Vehicle):
	def __init__(self,engine_type,car_category,**kwargs):
		super(Car,self).__init__(engine_type,**kwargs)
		self.car_category = car_category
		self.doors = 5
		self.wheels = 4
my_car = Car("VW-Golf","Saloon",engine_cc = 2000,color = "Red", max_speed = 120)
print my_car.doors
