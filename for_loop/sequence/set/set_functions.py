a={3,2,1,5,7,4,"hi",7.5,2+4j}
b={"x","y","z"}
a.add("hi")
a.update(b)
a.remove(1)
a.discard(2)
a.pop()
print(a)
for i in a:
    print(i)
print(len(a))
a.clear()
print(a)