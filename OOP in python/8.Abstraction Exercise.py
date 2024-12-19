from abc import ABC,abstractmethod
class shape:
    def __init__(self,	Radius):
        self.Radius=Radius

    def calculate_area(self):
        pass
class  Circle(shape):
    def calculate_area(self):
        area=3.1416*self.Radius
        print("The area of the circle is:"+str(area))
Radius=float(input("Enter the Radius :"))
ob1=Circle(Radius)
ob1.calculate_area()

