from employee import Employee

e1 = Employee(1, "Aman Kumar", "Software Engineer", 70000)
e2 = Employee(2, "Kumar Ashish", "Data Scientist", 80000)

e1.display_info()
print("-" * 20)
e2.display_info()

e1.increase_salary(10000)
e2.increase_salary(15000)

print("\nAfter Salary Update")
e1.display_info()
print("-" * 20)
e2.display_info()

e1.change_company("Microsoft Corporation")
e2.change_company("Google Corporation")

print("\nAfter changing company ")
e1.display_info()
print("-" * 20)
e2.display_info()
