#single and multilevel inharitance
class vehicle:#grandparent class
    brand=""
    model=""
    def start(self):
        print("vehicle started")
class car(vehicle):# parent class
    speed=""
    color=""
    def drive(self):
        print("car is driving")
class electric_car(car):
    battery_capacity=""
    def charge(self):
        print("Electric car is charging")

car1=car()
car1.brand="Toyota"
car1.model="Corolla"
car1.speed="120km/h"
car1.color="red"
car1.start()
ev1 = electric_car()
ev1.brand="Tesla"
ev1.model="Model s"
ev1.start()
ev1.drive()