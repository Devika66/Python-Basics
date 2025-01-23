n=int(input("Enter a number:"))
prime=2
while prime<n:
    if n%prime==0:
        break
    prime+=1
if prime==n:
    print("prime number")
else:
    print("not prime number")

 