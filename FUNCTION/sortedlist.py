def sortlist(list,l):
    for i in range(0,l-1):
        for j in range(0,l-i-1):
            if list[j]>list[j+1]:
                (list[j],list[j+1])=(list[j+1],list[j])
    return list




a=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("Enter a number"))
    a.append(num)
result=(sortlist(a,n))
print("sorted list=",result)
