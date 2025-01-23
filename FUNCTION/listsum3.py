def sumlist(s):
    return s

     
     
n=int(input("enter the range:"))

l1=[]
l2=[]

for i in range(n):
    num=int(input("enter the number:"))
    l1.append(num)
for i in range(n):
    num=int(input("enter the number:"))
    l2.append(num)
sum=0
for i in range(n):
    sum+=l1[i]+l2[i]

result=sumlist(sum)
print("sum of l1 and l2=",result)