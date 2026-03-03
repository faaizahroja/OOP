class vehicle:
    def __init__(self,speed):
        self.speed=speed
        self.distance= 100

class car(vehicle):
    def travel_time(self):
        return self.distance/self.speed
    
class bike(vehicle):
    def travel_time(self):
        return self.distance/self.speed
    


speed= float(input("Enter speed(km/h): "))



print("distance: ",car.distance,"km")
print("Car travel time: ",car.travel_time(),"hours")
print("Bike travel time: ",bike.travel_time(),"hours")
