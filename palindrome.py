n=int(input("Enter a number:"))
r=0
temp=n
while n!=0:
    d=n%10
    r=r*10+d
    n//=10

if(temp==r):
    print("number is palindrome")
else:
    print("not palindrome")