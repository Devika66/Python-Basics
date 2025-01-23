l=[5,3,32,6,7,22]
l1=[]
l2=[]
for i in range(6):
    if l[i]%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
print("The list of even numbers=",l1)
print("The list odd numbers=",l2)
    