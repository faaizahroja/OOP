class phone:
    brand=""
    model=""
    price=""
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.prince=price

    def showDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}k")
        
    def addTax(self,tax):
        self.price= self.price + (self.price*tax / 100)


b=input("Enter brand:")
m=input("Enter model:")
p=float(input("Enter price:"))
t=float(input("Enter tax percentage: "))

phone1=phone(b,m,p) #object creation and value initialization
phone2=phone("Samsung","Galaxy S21",799)

phone1.addTax(t)
phone1.showDetails()
