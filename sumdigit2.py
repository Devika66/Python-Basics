n=int(input("Enter a number:"))
sum=0
while n!=0:
    d=n%10
    sum+=d
    n//=10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)


