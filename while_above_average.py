
#Print sum of digit
# n=int(input("Enter a number:-"))
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print("Sum:-",sum)


#Reverse the number
# n=int(input("Enter a number:-"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print("Reverse number:-",rev)


#Check numeber is palidrome
# n=int(input("Enter a number:-"))
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if temp==rev:
#     print("Number is Palidrome")
# else:
#     print("Number is Not Palidrome")


# #Print multiplication table
# n=int(input("Enter number:-"))
# i=1
# while i<=10:
#     print(i,"*",n,"=",i*n)
#     i+=1


# # Prime number
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")

# else:
#     print(num, "is not a prime number")


# #Program to find the largest among n numbers
# n = int(input("Enter the number of elements: "))

# largest = int(input("Enter number 1: "))

# for i in range(2, n + 1):
#     num = int(input("Enter number " + str(i) + ": "))

#     if num > largest:
#         largest = num

# print("The largest number is:", largest)

# smallest numbers
n = int(input("Enter the number of elements: "))
smallest = int(input("Enter number 1: "))
for i in range(2, n + 1):
    num = int(input("Enter number " + str(i) + ": "))
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)