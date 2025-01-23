a=str(input("Enter a string:"))
r=""
for i in a:
    r=i+r
if r==a:
    print("palindrome")
else:
    print("not palindrome")