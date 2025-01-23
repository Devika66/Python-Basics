t=str(input("Enter a string:"))
vw="aeiouAEIOU"
count=0
for i in t:
    if i in vw:
        count+=1
print("count=",count)
    
