# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_student(self):
        self.show_person()
        print("Course:", self.course)


# Object creation
student1 = Student("Aman", 20, "B.Tech")

# Method call
student1.show_student()
