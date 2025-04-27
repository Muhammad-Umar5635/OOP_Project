class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        print("Show from Class B")

class C(A):
    def show(self):
        print("Show from Class C")

class D(B, C):
    pass

# Creating an object of class D
d = D()
d.show()
