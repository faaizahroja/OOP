from abc import ABC,abstractmethod
class magicShape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(magicShape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class circle(magicShape):
    def __init__(self, radius):
        self.radius = radius

class rectangle(magicShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        def area(self):
            return self.length *self.width
        
shapes = [square(4), circle(3), rectangle(4,5)]

for I in shapes:
    print(f'the area is:{I.area()}')    

