class Employee:

    # Constructor
    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.salary = salary

    # Display information
    def display_info(self):
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

    # Destructor
    def __del__(self):
        print("Employee object destroyed.")

name = input("Enter name: ")
age = int(input("Enter age: "))
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

# Create object
e1 = Employee(name, age, employee_id, salary)
e1.display_info()
