class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for s in self.students:
            print(f"Name: {s.name}, Marks: {s.marks}, Grade: {s.get_grade()}")


# usage
s1 = Student("Rahul", 75)
s2 = Student("Anita", 88)

manager = StudentManager()
manager.add_student(s1)
manager.add_student(s2)

manager.display_students()
