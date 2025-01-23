lower=int(input("enter the limit:"))
upper=int(input("enter the limit:"))
while lower<=upper:
    num=lower
    if num>1:
        i=2
        while i<=num:
            if num%i==0:
                break
            i+=1
        if i==lower:
            print(lower,end=" ")
        lower+=1
print()
            


          