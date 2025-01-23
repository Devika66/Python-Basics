a={1,2,7,3,"a","b","c","d",6+0j,1,2.7,"z"}
b={"x","y","z"}
#c=a.intersection(b)
#print(c)
#a.intersection_update(b)
#print(a)
c=a.symmetric_difference(b)
print(c)

a.symmetric_difference_update(b)
print(a)







#'''a.update(b)
#print(a)
#c=a.union(b)
#print(c)
