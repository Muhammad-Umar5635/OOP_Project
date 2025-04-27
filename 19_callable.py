class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance
m = Multiplier(5)

# Check if the object is callable
print(callable(m))  # Output: True

# Call the object like a function
result = m(10)
print(result)  # Output: 50
