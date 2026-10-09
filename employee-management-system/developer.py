from employee import Employee


class Developer(Employee):

    def __init__(
        self, employee_id, name, position, salary, programming_language
    ):
        super().__init__(employee_id, name, position, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.programming_language}"