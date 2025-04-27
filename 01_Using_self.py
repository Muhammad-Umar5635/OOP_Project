# Project 1 Using Self
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Student name:",self.name)
        print("Student Marks:",self.marks)

student1 = Student("Umar",93)
Student2 = Student("Imaan", 88)
student1.display()
print("-------")
Student2.display()



