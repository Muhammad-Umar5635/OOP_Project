from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,Width):
        self.lenght = length
        self.width = Width
    def area(self):
        return self.lenght * self.width

rect = Rectangle(5,4)
print("Area of the reactangle:",rect.area())