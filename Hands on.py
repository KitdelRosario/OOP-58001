class Person:
  def __init__(self,std, pre, mid, fin):
    self.__std = std
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin

  def Grade(self):
    return (self.__pre + self.__mid + self.__fin)/3

  def display(self):
    print("Name: ",self.__std)
    print("Prelims: ",self.__pre)
    print("Midterms: ",self.__mid)
    print("Finals: ",self.__fin)
    print("Average: ",self.Grade())
    print(" ")

class Student1(Person):
  pass
class Student2(Person):
  pass
class Student3(Person):
  pass

std1 = Student1("Student 1",95,89,78)
std1.display()

std2 = Student2("Student 2",51,90,78)
std2.display()

std3 = Student3("Student 3",80,79,68)
std3.display()

#mangling test (Double UnderScore)
std1.std = "kit"
std1.pre = 88
std1.mid = 77
std1.fin = 66
std1.display()