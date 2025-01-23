a=[]
b=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter number:"))
    a.append(num)
m=int(input("enter the limit:"))
for i in range(m):
    num=int(input("enter number:"))
    b.append(num)
for i in range(0,n-m+1):
    if a[i:i+m]==b:
        print(f"{b} is sublist of {a}")
        break
else:
        print(f"{b} is not sublist of {a}")
 
        





