# Create student records file

n = int(input("Enter number of students: "))

f = open("students.txt", "w")

f.write("RollNo,Name,Marks\n")

for i in range(n):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    f.write(roll + "," + name + "," + str(marks) + "\n")

f.close()

print("Student records saved successfully.")