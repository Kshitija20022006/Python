
n = int(input("Enter number of students: "))

f = open("attendance.txt", "w")

f.write("RollNo,Name,Present,Total\n")

for i in range(n):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    present = int(input("Enter days present: "))
    total = int(input("Enter total working days: "))

    f.write(roll + "," + name + "," + str(present) + "," + str(total) + "\n")

f.close()

print("\nAttendance records saved successfully!")
f = open("attendance.txt", "r")

records = f.readlines()

f.close()
records = records[1:]

print("\n--- Attendance Percentage ---")

for record in records:
    roll, name, present, total = record.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    print(name, ":", percentage, "%")


print("\n--- Students Having Attendance Below 75% ---")

for record in records:
    roll, name, present, total = record.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    if percentage < 75:
        print(roll, name, "-", percentage, "%")