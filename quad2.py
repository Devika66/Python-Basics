a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
x=b**2-4*a*c
if x==0:
    x1=-b/2*a
    print(f"x1={x1}")

elif x>0:
    x1=(-b+x**0.5)/2*a
    x2=(-b-x**0.5)/2*a
    print(f"x1={x1}")
    print(f"x2={x2}")
else:
    print("Imaginary roots ")