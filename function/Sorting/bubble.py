def sort(a,n):
    for i in range(0,n):
        for j in range(0,n-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            
    return a;

n=int(input("Enter radius:"))
a=[5,4,3,2,1];
sort(a,n)
for i in range(0,n):
    print("a[i]")