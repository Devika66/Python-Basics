a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))

if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Right Triangle")
else:
    print("Not right triangle")