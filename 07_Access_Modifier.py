class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected (convention)
        self.__ssn = ssn          # Private (name mangled)

# Creating an object
emp = Employee("Umar", 50000, "123-45-6789")

# Accessing variables
print("Public (name):", emp.name)         # ✅ Allowed
print("Protected (_salary):", emp._salary) # ⚠️ Allowed, but not recommended
#print("Private (__ssn):", emp.__ssn)      # ❌ Error: AttributeError
