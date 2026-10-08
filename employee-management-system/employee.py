class Employee:
    company_name = "edu Corporation"
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Company: {self.company_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary increased by ${amount:.2f}. New salary: ${self.salary:.2f}")

    def change_company(self, new_name):
        self.company_name = new_name
        print(f"Company name changed to: {self.company_name}")

    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        else:
            return False

    

        