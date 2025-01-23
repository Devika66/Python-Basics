l=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter the number:"))
    l.append(num)
large=l[0]
for i in range(1,n):
    if l[i]>large:
        large=l[i]
        large_index=i
l.pop(large_index)
l.insert(0,large)
second=l[1]
for i in range(2,n):
    if l[i]>second:
        second=l[i]
print("the second largest element is",second)

