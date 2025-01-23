list=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("Enter a number"))
    list.append(num)
print(list)
reverse=[]
for i in range(n-1,-1,-1):
    reverse.append(list[i])
print(reverse)

    
