lower=int(input("enter the limit:"))
upper=int(input("enter the limit:"))
while lower<=upper:
    num=lower
    t=0
    ex=len(str(lower))
    while num>0:
        d=num%10
        t+=d**ex
        num//=10
    if t==lower:
        print(lower,end=" ")
    lower+=1
print()