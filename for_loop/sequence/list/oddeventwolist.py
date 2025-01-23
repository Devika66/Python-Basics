a=[1,2,3,4,5,6]
b=[7,8,9,10]
a.extend(b)
b.clear()
for i in a:
    if i%2==0:
        b.append(i)
        a.remove(i)
    
    
print(a)
print(b)




    




    

    





    
    