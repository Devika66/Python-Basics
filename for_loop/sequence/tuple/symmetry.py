t=(2,3,3,2)
n=4
t=list(t)
r=[]
for i in range(n-1,-1,-1):
    r.append(t[i])
r=tuple(r)
t=tuple(t)
if r==t:
    print("symmetric tuple")
else:
    print("not symmetric")


    

