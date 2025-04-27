class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting the price...")
        if value >= 0:
            self._price = value
        else:
            print("Invalid price. Price must be positive.")

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Using the class
p = Product(100)

print(p.price)       # Getting the price
p.price = 150        # Setting the price
print(p.price)       # Getting the price again

del p.price          # Deleting the price
try:
    print(p.price)   # This will raise an AttributeError
except AttributeError as e:
    print(e)