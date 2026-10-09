class Employee:
    company_name = "edu Corporation"

    def __init__(self, employee_id, name, position, salary):
        if not self.is_valid_salary(salary):
            raise ValueError("Salary must be greater than 0")

        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Company: {self.company_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")

    def increase_salary(self, amount):
        if not self.is_valid_salary(amount):
            raise ValueError("Salary increment must be greater than 0")

        self.salary += amount
        print(
            f"Salary increased by ${amount:,.2f}. "
            f"New salary: ${self.salary:,.2f}"
        )

    @classmethod
    def change_company(cls, new_name):
        if not new_name or not new_name.strip():
            raise ValueError("Company name cannot be empty")

        cls.company_name = new_name.strip()
        print(f"Company name changed to: {cls.company_name}")

    @staticmethod
    def is_valid_salary(salary):
        return (
            isinstance(salary, (int, float))
            and not isinstance(salary, bool)
            and salary > 0
        )