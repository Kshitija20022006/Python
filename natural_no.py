n=int(input("Enter number n:"))

print("Natural numbers:")
for i in range(1,n+1):
    print(i)

print("Odd numbers:")
for i in range(n+1):
    if i%2!=0:
            print(i)

print("Even numbers:")
for i in range(n+1):
    if i%2==0:
            print(i)

# print("Even number up to n square:")
# for i in range(0,n**2+1):
#      print(2**i)