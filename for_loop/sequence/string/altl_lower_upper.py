s="pythonDJanGO"
r=""
u=True
for i in s:
    if u:
        r+=i.upper()
    else:
        r+=i.lower()
    u=not u
print(r)