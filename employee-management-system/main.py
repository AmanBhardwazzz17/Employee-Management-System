from employee import Employee
from developer import Developer


# Create objects
e1 = Employee(1, "Aman Kumar", "Software Engineer", 70000)

e2 = Developer(
    2, "Kumar Ashish", "Data Scientist", 80000, "Python"
)

# Display employee information
print("Employee Details")
e1.display_info()

print("-" * 30)

print("Developer Details")
e2.display_info()

# Increase salary
e1.increase_salary(5000)
e2.increase_salary(10000)

print("\nAfter Salary Update")
e1.display_info()

print("-" * 30)

e2.display_info()

# Change company for both classes
Employee.change_company("Microsoft Corporation")

print("\nAfter Changing Company")
e1.display_info()

print("-" * 30)

e2.display_info()

# Validate salary
print("\nSalary Validation")
print(Employee.is_valid_salary(70000))  # True
print(Employee.is_valid_salary(-5000))  # False
print(Employee.is_valid_salary(0))      # False

# Test invalid salary increment
try:
    e1.increase_salary(-2000)
except ValueError as exc:
    print(f"\nError: {exc}")

# String representation of Developer
print("\nDeveloper Summary")
print(e2)