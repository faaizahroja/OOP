class shape:
    def area(self,side1,side2=0):
        if side2==0:
            print("area is: ",3.14*side1*side2)
        else:
            print("area is: ",side1*side2)

circle=shape()
circle.area(3)
rectangle=shape()
circle.rectangle( 4,5)

circle(50,90)