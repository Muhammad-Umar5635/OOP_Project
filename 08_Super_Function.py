class Person:
    def __init__(self,name):
        self.name = name
        print("Super Class:",self.name)

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
        print("Child teacher: ",self.subject) 
Person("Usman")
Teacher("Umar","Mathematics")
    
    