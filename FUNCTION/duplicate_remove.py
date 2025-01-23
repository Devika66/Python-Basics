def duplicate(l):
    r=[]
    for i in l:
        if i not in r:
            r.append(i)
    return r

l1=[]
n=int(input("enter range:"))
for i in range(n):
    num=int(input("enter the number:"))
    l1.append(num)
print(duplicate(l1))

