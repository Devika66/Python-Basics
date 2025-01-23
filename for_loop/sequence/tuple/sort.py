a=(33,6,1,66,3)
a=list(a)
n=5
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            (a[j],a[j+1])=(a[j+1],a[j])
print("sorted tuple=",tuple(a))
