d={"name":"devika","place":"pta","age":24}
print(type(d))
print(d)
print(d["name"] in d)
print(d["name"])
d["age"]=23
print(d)
d.update({"marks":5,"grade":"A+" })
print(d)  
c=d.keys()
print(c) 
c=d.values() 
print(c) 
c=d.items()
print(c)
d.pop("age")
print(d)
d.popitem()
print(d)
for i in d.items():
    print(i)
                  
