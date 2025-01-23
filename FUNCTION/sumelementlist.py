def sumlistelement(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

n=int(input("enter the no of elements:"))
l=[]
for i in range(n):
    num=int(input("enter the numbers:"))
    l.append(num)
result=sumlistelement(l)
print(f"sum of {l}={result}")



