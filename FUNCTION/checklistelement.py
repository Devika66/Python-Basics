def check(l,a):
    for i in l:
        if i==a:
            return("yes")
            break
            
    else:
        return("no")
l1=[2,3,4,5]
a=4
print(check(l1,a))