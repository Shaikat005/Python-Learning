def add(X,Y):
    sum=X+Y
    return sum

def greatest(A,B):
    if(A>B):
        return A
    else:
        return B

result=add(10,20)
print(result)

print("The greatest number is: ",(greatest(20,10)))