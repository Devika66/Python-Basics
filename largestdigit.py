n=int(input("Enter a number:"))
l=0
while n!=0:
    d=n%10
    if d>l:
        l=d
    n//=10
print("The largest digit is",l)
