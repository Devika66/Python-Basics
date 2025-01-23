n=int(input("Enter a number:"))
sum=0
prod=1
while n>0:
    d=n%10
    sum+=d
    prod*=d
    n//=10
if sum==prod:
    print("spynumber")
else:
    print("not spynumber")


