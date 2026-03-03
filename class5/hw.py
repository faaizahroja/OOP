from abc import ABC,abstractmethod

class Appliance(ABC):
    @abstractmethod
    def power_usage(self):
       pass

class Fan(Appliance):
    def __init__(self,hours):
        self.hours =hours

    def power_usage(self):
        return 75 * self.hours
    

class Fridge(Appliance):
    def __init__(self,hours):
        self.hours =hours

    def power_usage(self):
        return 200 * self.hours
    

fan_hour = float(input("write fan using hour: "))
fri_hour = float(input("write fridge using hour: "))

fan = Fan(fan_hour)
fridge = Fridge(fri_hour)

total_power = fan.power_usage() + fridge.power_usage()

print("Total power used in a day : ",total_power,"watt hours")

    


