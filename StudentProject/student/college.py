def college_info():
    M1=int(input("\nEnter M1 Marks:-"))
    cc=int(input("Enter CC Marks:-"))
    daa=int(input("Enter DAA Marks:-"))
    apc=int(input("Enter APC Marks:-"))
    t=((M1+cc+daa+apc)/400)*100
    cgpa=t/10

    print("\n---Student College Information---")
    print("M1 marks:-",M1)
    print("CC Marks:-",cc)
    print("DAA Marks:-",daa)
    print("APC Marks:-",apc)
    print("Percentage :-",t)
    print("CGPA:-",cgpa)