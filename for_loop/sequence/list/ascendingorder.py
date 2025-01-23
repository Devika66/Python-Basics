a=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("Enter a number"))
    a.append(num)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            (a[j],a[j+1])=(a[j+1],a[j])
print("sorted list",a)


