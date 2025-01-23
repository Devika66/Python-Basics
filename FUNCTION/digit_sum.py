def sumdigit(n):
    sum=0
    while n!=0:
        d=n%10
        sum+=d
        n//=10
    return(f"sum={sum}")
num=int(input("enter a number:"))
print(sumdigit(num))