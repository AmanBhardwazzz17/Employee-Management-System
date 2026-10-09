<div align="center">

# 💼 Employee Management System

### Python · Object-Oriented Programming · Software Development

A structured Python project demonstrating real-world Object-Oriented Programming
concepts through employee management, salary validation, and inheritance.

<br>

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concepts-OOP-2563EB?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-F59E0B?style=for-the-badge)

</div>

---

## 📌 Project Overview

The Employee Management System is a hands-on Python project developed
to build a strong foundation in Object-Oriented Programming.

It demonstrates how classes, objects, inheritance, method overriding,
validation, and exception handling can be used to create maintainable
and reusable code.

The project is being developed incrementally as new concepts are learned.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 👤 Employee Management

Create employee objects and display employee information, including
employee ID, name, position, and salary.

</td>
<td width="50%">

### 💰 Salary Management

Increase employee salaries with validation to prevent invalid increments.

</td>
</tr>
<tr>
<td width="50%">

### 🏢 Company Management

Update the shared company name using a class method.

</td>
<td width="50%">

### 🛡️ Input Validation

Validate salary values and raise exceptions when invalid values are provided.

</td>
</tr>
<tr>
<td width="50%">

### 🧬 Inheritance

Extend the Employee class through a Developer class and reuse existing functionality.

</td>
<td width="50%">

### 🔄 Method Overriding

Customize developer information display and use `super()` to reuse
parent-class functionality.

</td>
</tr>
</table>

---

## 🧠 OOP Concepts Implemented

| Concept | Implementation |
|:---|:---|
| Classes & Objects | `Employee`, `Developer` |
| Constructor | `__init__()` |
| Instance Variables | `name`, `salary`, `position`, `employee_id` |
| Class Variables | `company_name` |
| Instance Methods | `display_info()`, `increase_salary()` |
| Class Methods | `@classmethod` |
| Static Methods | `@staticmethod` |
| Inheritance | `Developer(Employee)` |
| Method Overriding | Customized `display_info()` |
| Parent Class Access | `super()` |
| Exception Handling | `raise ValueError`, `try-except` |
| Magic Methods | `__str__()` |

---

## 🛠️ Technology Stack

<table>
<tr>
<td align="center" width="25%">

🐍

**Python 3**

Core Language

</td>
<td align="center" width="25%">

🧱

**OOP**

Code Structure

</td>
<td align="center" width="25%">

🔧

**Git**

Version Control

</td>
<td align="center" width="25%">

💻

**VS Code**

Development

</td>
</tr>
</table>

---

## 📂 Project Structure

```text
employee-management-system/
│
├── employee.py       # Base Employee class
├── developer.py      # Developer class and inheritance
├── manager.py        # Manager class (planned)
├── main.py           # Main application entry point
├── utils.py          # Utility functions
├── tests/
│   └── test_employee.py
├── .gitignore        # Files excluded from Git
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3
- Git (optional)
- Visual Studio Code or another code editor

### Run the Project

**1. Clone the repository**

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

**2. Navigate to the project directory**

```bash
cd employee-management-system
```

**3. Run the application**

```bash
python3 main.py
```

---

## 💻 Example Output

```text
Employee Details
Company: edu Corporation
Employee ID: 1
Name: Aman Kumar
Position: Software Engineer
Salary: $70,000.00

Salary increased by $5,000.00. New salary: $75,000.00

Company name changed to: Microsoft Corporation
```

*Output shown is an example of the application's current functionality.*

---

## 🗺️ Development Roadmap

- [x] Create Employee class and objects
- [x] Implement constructors and instance variables
- [x] Add salary validation
- [x] Implement class and static methods
- [x] Implement inheritance with Developer
- [x] Practice method overriding and `super()`
- [x] Handle invalid salary increments
- [x] Implement `__str__()`
- [ ] Add Manager class with `team_size`
- [ ] Implement encapsulation
- [ ] Expand automated unit tests
- [ ] Add employee search and update functionality
- [ ] Integrate a database

---

## 🎯 Project Goals

- Strengthen Python programming fundamentals.
- Apply OOP concepts through practical coding.
- Write reusable and maintainable code.
- Improve debugging and exception-handling skills.
- Prepare for technical interviews and software development internships.

---

<div align="center">

### Built with Python and a commitment to continuous learning.

**Employee Management System · Personal Learning Project**

</div>