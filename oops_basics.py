# OOPS Basics in Python

#Class and Object
class Student:
  def __init__(self,name,roll_no):
    self.name=name
    self.roll_no=roll_no

  def display_details(self):
    print("Name:",self.name)
    print("Roll_no:",self.roll_no)

# Creating object
s1=Student("Muskan",101)
s1.display_details()

print("-"*30)

# Another example
class Calculator:
  def add(self,a,b):
    print("Addition:",a+b)

  def subtract(self,a,b):
    print("Subtraction:",a-b)
  
calc=Calculator()
calc.add(10,5)
calc.subtract(10,5)
