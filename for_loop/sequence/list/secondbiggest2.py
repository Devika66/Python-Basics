l=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter the number:"))
    l.append(num)
big=l[0]
for i in range(1,n):
    if l[i]>big:
        big=l[i]
i=0
while(1):
    if l[i]!=big:
        sbig=l[i]
        break
    i+=1
for i in range(i+1,n):
    if l[i]<big and l[i]>sbig:
        sbig=l[i]
print("second largest element is",sbig)