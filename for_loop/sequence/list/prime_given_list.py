l=[]
n=int(input("enter the limit:"))
for i in range(n):
    num=int(input("enter number:"))
    l.append(num)
for i in l:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    else:
        print(i)

    
    
            
            
        

        



