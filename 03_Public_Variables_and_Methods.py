# project 03
class Car:
    def __init__(self,brand):
        self.brand = brand
    @classmethod
    def start(cls):
        print(f"Your {cls.brand} is start now.")

car = Car("BMW")
print(f"Your car brand name is: {car.brand}")
car.start()