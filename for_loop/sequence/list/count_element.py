l1=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter the number:"))
    l1.append(num)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    c=0
    for j in l1:
        if j==i:
            c+=1
    print("count of",i,"=",c)


