n=int(input("Enter a number:"))
temp=n
s=0
while n!=0:
    d=n%10
    f=1
    while d>1:
        f*=d
        d-=1
    s+=f
    n//=10
if temp==s:
    print("strong number")
else:
    print("not strong number")

 