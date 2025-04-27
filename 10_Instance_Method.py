class Dog:
    def __init__(self, name, breed):
        self.name = name         # instance variable
        self.breed = breed       # instance variable

    def bark(self):
        print(f"{self.name} says: Woof woof!")

dog = Dog("Buddy", "Garman Shepherd")

dog.bark()