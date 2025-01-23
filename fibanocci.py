n=10
f1=0
f2=1
if n<=0:
    print("no fibanocci series")
elif n==1:
    print(f1)
elif n==2:
    print(f1)
    print(f2)
else:
    print(f1)
    print(f2)
    while n>0:
        f3=f1+f2
        print(f3)
        f1,f2=f2,f3
        n-=1