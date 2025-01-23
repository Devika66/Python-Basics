m=int(input("Enter mark of the student:"))
if m>=90:
    print("Outstanding")
elif m>=85 and m<90:
    print("A+")
elif m>=80 and m<85:
    print("A")
elif m>=75 and m<80:
    print("B+")
elif m>=70 and m<75:
    print("B")
elif m>=65 and m<70:
    print("C+")
elif m>=60 and m<65:
    print("C")
elif m>=55 and m<60:
    print("D")
elif m>=50 and m<55:
    print("Pass")
else:
    print("Fail")
