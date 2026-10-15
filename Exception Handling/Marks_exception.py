
while True:
        try:
            apc = int(input("Enter marks of APC: "))
            if 0<apc<100:
                  print("Marks of APC =", apc)
            break
                           
        except:
            print("Invalid input! Enter integer again.")

while True:
         try:
              cc=int(input("Enter marks of CC:"))
              if 0<cc<100:
                    print("Marks of CC =", cc)
              break
         except:
             print("Invalid input! Enter integer again.")

while True:
         try:
              ajt=int(input("Enter marks of AJT:"))
              try:
                    if 0<ajt<100:
                          print("Marks of AJT =", ajt)
              except:
                    print("Invalid input! Enter integer again.")
              break
         except:
             print("Invalid input! Enter integer again.")

while True:
         try:
              os=int(input("Enter marks of OS:"))
              if 0<os<100:
                    print("Marks of OS =", os)
              break
         except:
             print("Invalid input! Enter integer again.")

total=apc+cc+ajt+os
per=(total/400)*100
print("Total marks:-",total)
print("Percentage :-",per)