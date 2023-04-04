class DistanceConversion:
  def __init__(self,distance):
    self.__distance = distance

  def mtoc(self):
    return self.__distance*100

  def mtok(self):
    return self.__distance/100

  def mtoi(self):
    return self.__distance*39.37

  def display(self):
    print("Centimeter: ",self.mtoc())
    print("Kilometer: ", self.mtok())
    print("inches: ", self.mtoi())

Distance = DistanceConversion(float(input("Enter the distance in meters: ")))
Distance.display()
