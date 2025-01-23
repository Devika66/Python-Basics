def sumlist(list):
    return list
        
    

n=int(input("enter the range:"))
l1=[]
l2=[]
l3=[]
for i in range(n):
    num=int(input("enter the number:"))
    l1.append(num)
for i in range(n):
    num=int(input("enter the number:"))
    l2.append(num)
for i in range(n):
    l3.append(l1[i] +l2[i])
result=sumlist(l3)
print(f"sum of {l1} and {l2}={l3}")




