# # #Student Grade System
# students = ["Amit", "Rahul", "Sneha", "Priya"]
# grades = [75, 82, 90, 68]
# name = input("Enter new student name: ")
# grade = int(input("Enter grade: "))
# students.append(name)
# grades.append(grade)
# name = input("\nEnter student name to update grade: ")
# if name in students:
#     index = students.index(name)
#     new_grade = int(input("Enter new grade: "))
#     grades[index] = new_grade
# else:
#     print("Student not found.")
# name = input("\nEnter student name to remove: ")
# if name in students:
#     index = students.index(name)
#     students.pop(index)
#     grades.pop(index)
#     print("Student removed.")
# else:
#     print("Student not found.")
# if len(grades) > 0:
#     average = sum(grades) / len(grades)
#     print("\nAverage grade:", average)
# #     # Highest and lowest grade
#     print("Highest grade:", max(grades))
#     print("Lowest grade:", min(grades))
# else:
#     print("No students available.")
# print("\nStudent Grade List:")
# for i in range(len(students)):
#     print(students[i], ":", grades[i])


##------Program to calculate distance between 2 points-------
# import math
# # Function to calculate Euclidean distance between two points
# def distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
# # Function to find the point farthest from origin
# def farthest_from_origin(points):
#     farthest_point = points[0]
#     max_distance = distance((0, 0), points[0])
#     for point in points:
#         d = distance((0, 0), point)
#         if d > max_distance:
#             max_distance = d
#             farthest_point = point
#     return farthest_point, max_distance
# # Taking input
# n = int(input("Enter number of points: "))
# points = []
# for i in range(n):
#     x, y = map(float, input(f"Enter x and y coordinates of point {i+1}: ").split())
#     points.append((x, y))
# # Display points
# print("\nPoints:", points)
# # Calculate distance between two given points
# p1 = points[0]
# p2 = points[1]
# print(f"Distance between {p1} and {p2} = {distance(p1, p2):.2f}")
# # Find farthest point from origin
# point, dist = farthest_from_origin(points)
# print(f"Point farthest from origin: {point}")
# print(f"Distance from origin: {dist:.2f}")


# ##----Design to manage web server configuration
# server_ip = ("192.168.1.10",)

# # Allowed IPs stored in a list (mutable)
# allowed_ips = ["192.168.1.2", "192.168.1.3", "192.168.1.4"]

# # Function to update allowed IPs
# def update_allowed_ips(new_ip):
#     if new_ip not in allowed_ips:
#         allowed_ips.append(new_ip)
#         print("Allowed IP added successfully.")
#     else:
#         print("IP is already in the allowed list.")

# # Function to display configuration
# def display_configuration():
#     print("\nServer Configuration")
#     print("--------------------")
#     print("Server IP:", server_ip[0])
#     print("Allowed IPs:", allowed_ips)

# # Display original configuration
# display_configuration()

# # Update allowed IPs
# new_ip = input("\nEnter new IP address to allow: ")
# update_allowed_ips(new_ip)

# # Display updated configuration
# display_configuration()

# # Attempt to change server_ip
# print("\nServer IP is stored in a tuple, so it cannot be changed.")



####-------Write a program to manage 2 different projects in your company.
# A=set(input("Enter Employee for Project A: ").split())
# B=set(input("Enter Employee for Project B: ").split())
# print("Employes working on both Projects:",A.intersection(B))
# print("Employee working on only A project",A.difference(B))
# print("Employee working on only B project",B.difference(A))
# print("Employees working on both projects",A.union(B))



####-------Simple Text Analysis Tool(one task)
# A=input("Enter text: ").split()
# c=str(A)
# count=0
# f={}
# vowels="aeiouAEIOU"
# for i in A:
#     count+=1
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# B=sum(c.count(vowel)for vowel in vowels)
# print("Total Number of words: ",count)
# print(f)
# print("Number of vowels present: ",B)



####----# Program to analyze vocabulary used in two different books
# # Example text from Book 1
# book1 = """
# Python is a powerful programming language.
# Python is easy to learn and easy to use.
# """

# # Example text from Book 2
# book2 = """
# Python is widely used for programming and data analysis.
# It is easy to learn Python.
# """

# # Convert the text to lowercase and split it into individual words
# # set() automatically removes duplicate words
# words_book1 = set(book1.lower().split())
# words_book2 = set(book2.lower().split())

# # Find all unique words from both books using union
# all_unique_words = words_book1.union(words_book2)

# # Find common words present in both books using intersection
# common_words = words_book1.intersection(words_book2)

# # Find words that are only in Book 1 and not in Book 2
# unique_to_book1 = words_book1.difference(words_book2)

# # Find words that are only in Book 2 and not in Book 1
# unique_to_book2 = words_book2.difference(words_book1)

# # Display unique words in each book
# print("Unique words in Book 1:")
# print(words_book1)

# print("\nUnique words in Book 2:")
# print(words_book2)

# # Display common words
# print("\nCommon words in both books:")
# print(common_words)

# # Display words unique to Book 1
# print("\nWords unique to Book 1:")
# print(unique_to_book1)

# # Display words unique to Book 2
# print("\nWords unique to Book 2:")
# print(unique_to_book2)

# # Display the total number of unique words across both books
# print("\nTotal number of unique words across both books:")
# print(len(all_unique_words))



#####------Inventory Management System
# inventory = {}
# # Function to add a new product
# def add_product():
#     name = input("Enter product name: ")
#     quantity = int(input("Enter quantity: "))

#     if name in inventory:
#         print("Product already exists!")
#     else:
#         inventory[name] = quantity
#         print("Product added successfully.")

# # Function to update product quantity
# def update_product():
#     name = input("Enter product name to update: ")

#     if name in inventory:
#         quantity = int(input("Enter new quantity: "))
#         inventory[name] = quantity

#         # Remove product if quantity becomes 0
#         if quantity == 0:
#             del inventory[name]
#             print("Product is sold out and removed.")
#         else:
#             print("Quantity updated successfully.")
#     else:
#         print("Product not found.")

# # Function to remove a product
# def remove_product():
#     name = input("Enter product name to remove: ")

#     if name in inventory:
#         del inventory[name]
#         print("Product removed successfully.")
#     else:
#         print("Product not found.")

# # Function to display product with highest stock
# def highest_stock():
#     if len(inventory) == 0:
#         print("Inventory is empty.")
#     else:
#         product = max(inventory, key=inventory.get)
#         print("Product with highest stock:", product)
#         print("Quantity:", inventory[product])

# # Function to display total unique products
# def total_products():
#     print("Total unique products:", len(inventory))

# # Function to display inventory
# def display_inventory():
#     if len(inventory) == 0:
#         print("Inventory is empty.")
#     else:
#         print("\nInventory:")
#         for name, quantity in inventory.items():
#             print(name, ":", quantity)

# # Main program
# while True:
#     print("\n----- INVENTORY SYSTEM -----")
#     print("1. Add Product")
#     print("2. Update Quantity")
#     print("3. Remove Product")
#     print("4. Display Highest Stock")
#     print("5. Display Total Products")
#     print("6. Display Inventory")
#     print("7. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         add_product()

#     elif choice == 2:
#         update_product()

#     elif choice == 3:
#         remove_product()

#     elif choice == 4:
#         highest_stock()

#     elif choice == 5:
#         total_products()

#     elif choice == 6:
#         display_inventory()

#     elif choice == 7:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice!")



#####------Anagram Checker
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# # Function to normalize the string
# def normalize_string(text):
#     result = ""

#     for ch in text:
#         if ch.isalnum():
#             result += ch.lower()

#     return result

# # Function to count character frequency
# def character_frequency(text):
#     frequency = {}

#     for ch in text:
#         if ch in frequency:
#             frequency[ch] += 1
#         else:
#             frequency[ch] = 1

#     return frequency

# # Normalize both strings
# str1 = normalize_string(str1)
# str2 = normalize_string(str2)

# # Compare character frequencies
# if character_frequency(str1) == character_frequency(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# ####------Attendance Management System-----
# # Dictionary to store attendance
# attendance = {}

# # Days of the week
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Take attendance input for each day
# for day in days:
#     students = input("Enter students attended on " + day + " (separated by comma): ")

#     # Convert input into a set
#     student_set = set()
#     for name in students.split(","):
#         name = name.strip()
#         if name != "":
#             student_set.add(name)

#     attendance[day] = student_set

# # Find students who attended all classes
# all_students = set.intersection(*attendance.values())

# # Find students who attended only one class
# all_attended = set.union(*attendance.values())

# only_one = set()

# for student in all_attended:
#     count = 0
#     for day in days:
#         if student in attendance[day]:
#             count += 1
#     if count == 1:
#         only_one.add(student)

# # Total unique students
# total_students = len(all_attended)

# # Display results
# print("\n----- ATTENDANCE REPORT -----")
# print("Students who attended all classes:")
# print(all_students)
# print("\nStudents who attended only one class:")
# print(only_one)
# print("\nTotal unique students:", total_students)



#####------Character Frequency Counter

# Take input from user
text = input("Enter a string: ")

# Ask user for case option
choice = input("Ignore case? (yes/no): ")

# Convert to lowercase if user chooses to ignore case
if choice.lower() == "yes":
    text = text.lower()

# Dictionary to store character frequency
frequency = {}

# Count each character
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Sort dictionary by frequency in descending order
sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

# Display result
print("\nCharacter Frequency:")

for ch, count in sorted_frequency:
    if ch == " ":
        print("[space] :", count)
    else:
        print(ch, ":", count)