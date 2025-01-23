def sumdigit(n):
    sum=0
    while n!=0:
        d=n%10
        sum+=d
        n//=10
    return(sum)
a=int(input("enter number:"))
print(sumdigit(a))

