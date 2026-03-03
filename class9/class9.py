#polymorphism example in python

class car:
    def start(self):
        return"Car is starting with a key"
    
class boat:
    def start(self):
        return"boat is starting with a button"
    
class airplane:
    def start(self):
        return"airplane is starting with a lever"
    
#polymorphic function
def vehicle_start(vehicle):
    print(vehicle.start())

# creating objects
my_car = car()
my_boat = boat()
my_airplane = airplane()
#using polymorphism to start different vehicles
for vehivle in (my_car, my_boat, my_airplane):
    vehicle_start(vehicle)
