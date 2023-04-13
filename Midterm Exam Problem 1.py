class Circle:
  def __init__(self,radius):
   self.radius = radius

  def area(self):
    return 3.1416*self.radius**2

  def perimeter(self):
    return 2*3.1416*self.radius

  def display(self):
    print("Area: ",self.area())
    print("Perimeter: ",self.perimeter())

circle = Circle(float(input("Please Enter the Radius: ")))
circle.display()
