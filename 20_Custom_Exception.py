# Step 1: Define a custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    pass

# Step 2: Define a function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Step 3: Using try...except to handle the exception
try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
    print("Access granted. You are eligible.")
except InvalidAgeError as e:
    print(f"Access denied: {e}")
except ValueError:
    print("Invalid input: Please enter a valid number.")
