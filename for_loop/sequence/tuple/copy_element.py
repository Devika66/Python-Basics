a=(1,4,5,"hi",True,2+3j,7)
a=list(a)
b=[4,True,7]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(tuple(c))
   