def sublist(l1,l2,l,r):
    for i in range(0,l-r+1):
        if a[i:i+r]==b:
            return(f"{l2} is sublist of {l1}")
            break
    else:
        return(f"{l2} is not sublist of {l1}")




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
print(sublist(a,b,n,m))

