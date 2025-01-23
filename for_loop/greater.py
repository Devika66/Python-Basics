n=int(input("Enter the limit:"))
b=0
for i in range (n):
    no=int(input("Enter the number:"))
    if no>b:
        b=no
print("The greatest number is",b)
    