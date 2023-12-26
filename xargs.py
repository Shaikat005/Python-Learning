#xrags- It is used to pass any number of arguments.

def add(*number):
    sum=0;
    for i in number:
        sum=sum+i
    return sum;

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))