from abc import ABC, abstractmethod

class Parent(ABC):
    def show(self):
        pass

class Child(Parent):
    def show(self):
        print("This is the implementation of the abstract method.")


class Child2(Parent):
    def show(self):
        print("This is another implementation of the abstract method.")


obj1=Child()
obj1.show()
obj2=Child2()
obj2.show()

