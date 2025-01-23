l=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter the number:"))
    l.append(num)
large=0
for i in l:
    if i>large:
        large=i
l.insert(0,large)
result=[]
for i in l:
    if i not in result:
        result.append(i)
second=0
for i in range(1,n):
    if result[i]>second:
        second=result[i]
print("the second largest element is",second)



#second=0
#for i in range(1,5):
   # if l[i]>second:
        #second=l[i]
#print("The second largest element is",second)

