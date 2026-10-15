class Student:

    # Constructor
    def __init__(self, name, age, course, M1, cc, daa, apc):
        self.name = name
        self.age = age
        self.course = course
        self.M1 = M1
        self.cc = cc
        self.daa = daa
        self.apc = apc

        self.t = ((M1 + cc + daa + apc) / 400) * 100
        self.cgpa = self.t / 10

        print("\nStudent object created!")

    def student_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def college_info(self):
        print("\n--- Student College Information ---")
        print("M1 Marks:", self.M1)
        print("CC Marks:", self.cc)
        print("DAA Marks:", self.daa)
        print("APC Marks:", self.apc)
        print("Percentage:", self.t)
        print("CGPA:", self.cgpa)

    # Destructor
    def __del__(self):
        print("\nStudent object destroyed!")

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

M1 = int(input("\nEnter M1 Marks: "))
cc = int(input("Enter CC Marks: "))
daa = int(input("Enter DAA Marks: "))
apc = int(input("Enter APC Marks: "))

s = Student(name, age, course, M1, cc, daa, apc)

s.student_info()
s.college_info()

del s