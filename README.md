<div align="center">

# Employee Management System

### A Python Object-Oriented Programming Project

A practical project demonstrating object-oriented programming concepts
through employee information management, salary validation, and inheritance.

<br>

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-Object--Oriented%20Programming-6C63FF?style=flat-square)

</div>

---

## Overview

The Employee Management System is a Python project developed to
practice object-oriented programming through a structured,
real-world-inspired application.

The project currently supports employee information display,
salary updates with validation, company name changes, and a
Developer class built using inheritance.

It is being developed incrementally as new programming concepts
are learned and implemented.

## Features

- **Employee Management** — Create employee objects and display their information.
- **Salary Management** — Increase salaries with input validation.
- **Salary Validation** — Reject invalid salary values.
- **Company Management** — Update the shared company name.
- **Inheritance** — Extend the Employee class through a Developer class.
- **Method Overriding** — Customize the developer information display.
- **Exception Handling** — Handle invalid salary increments.
- **String Representation** — Display developer objects using `__str__()`.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Object-Oriented Programming | Application structure and reusable classes |
| Git | Version control |
| Visual Studio Code | Development environment |

## Project Structure

```text
employee-management-system/
├── employee.py       # Employee class and core functionality
├── developer.py      # Developer class and inheritance
├── main.py           # Application entry point
├── tests/            # Test files
├── utils.py           # Utility functions
├── .gitignore         # Git exclusion rules
└── README.md          # Project documentation
```

## OOP Concepts Implemented

| Concept | Usage |
|---|---|
| Classes and Objects | `Employee` and `Developer` |
| Constructor | `__init__()` |
| Instance Variables | Employee ID, name, position, salary |
| Class Variables | Shared company name |
| Instance Methods | Display employee details and increase salary |
| Class Methods | Update the company name |
| Static Methods | Validate salary values |
| Inheritance | `Developer(Employee)` |
| Method Overriding | Customize `display_info()` |
| `super()` | Initialize inherited employee attributes |
| Exception Handling | `raise ValueError` and `try-except` |
| Magic Methods | `__str__()` |

## Getting Started

### Prerequisites

- Python 3 installed on your system.
- A terminal or code editor such as Visual Studio Code.

### Run Locally

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd employee-management-system
```

**3. Run the application**

```bash
python3 main.py
```

## Example Output

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

## Development Roadmap

- [x] Employee class and object creation
- [x] Constructor and instance variables
- [x] Salary validation
- [x] Class methods and static methods
- [x] Developer class and inheritance
- [x] Method overriding and `super()`
- [x] Exception handling
- [x] String representation with `__str__()`
- [ ] Manager class
- [ ] Encapsulation
- [ ] Automated unit testing
- [ ] Employee search and update functionality
- [ ] Database integration

## Learning Objectives

This project is intended to strengthen practical understanding of
Python OOP, code organization, validation, exception handling,
inheritance, and maintainable programming practices.

## Project Status

**In Progress** — New features and OOP concepts will be added as
development and learning continue.

---

<div align="center">

Developed as part of a hands-on Python learning journey.

</div>