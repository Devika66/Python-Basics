t=(1,4,5,6,7)
n=5
t=list(t)
reverse=[]
for i in range(n-1,-1,-1):
    reverse.append(t[i])
print(tuple(reverse))

