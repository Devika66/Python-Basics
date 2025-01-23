a=input("enter a string:")
b=a.upper()
upper=0
lower=0
for i in a:
    if i in b:
        upper+=1
    else:
        lower+=1
print("uppercase count=",upper)
print("lowercase count=",lower)

    



