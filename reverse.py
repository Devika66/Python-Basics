n=int(input("Enter the number:"))
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n//=10
print(r)
