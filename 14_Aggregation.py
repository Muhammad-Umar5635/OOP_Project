class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: storing reference

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()

emp1 = Employee("Muhammad Umar")

dept1 = Department("Finance", emp1)

# Display information
dept1.show_department()
