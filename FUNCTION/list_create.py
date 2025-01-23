def list(n):
    l=[]
    for i in range(n):
        num=int(input("enter number:"))
        l.append(num)
    return l
r=int(input("enter range:"))
print(list(r))

