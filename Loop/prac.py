n=int(input("Enter the value of rows:"));
for i in range(1,6+1,1):
    for j in range(1,(4*(6-i))+1,1):
        print(" ",end="")
    for k in range(1,i+1,1):
        print("bol ",end="")
    print("\n")
