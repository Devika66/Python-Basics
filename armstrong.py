n=input("Enter a number:")
ex=len(n)
n=int(n)
temp=n
s=0
while n>0:
    d=n%10
    s=s+d**ex
    n//=10
if temp==s:
    print("Armstrong number")
else:
    print("not armstrong")
