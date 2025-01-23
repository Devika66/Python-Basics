a=[]
b=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter number:"))
    a.append(num)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            (a[j],a[j+1])=(a[j+1],a[j])
print("sorted list",a)

m=int(input("enter the limit:"))
for i in range(m):
    num=int(input("enter number:"))
    b.append(num)
for i in range(0,m-1):
    for j in range(0,m-i-1):
        if b[j]>b[j+1]:
            (b[j],b[j+1])=(b[j+1],b[j])
print("sorted list",b)

c=a+b
for i in range(0,n+m-1):
    for j in range(0,n+m-i-1):
        if c[j]>c[j+1]:
            (c[j],c[j+1])=(c[j+1],c[j])
print("sorted list",c)

