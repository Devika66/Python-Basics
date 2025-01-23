u=int(input("Enter unit:"))
if u<=100:
    amount=u*0.5
elif u>100 and u<=150:
    amount=u*0.75
elif u>150 and u<=200:
    amount=u*1
else:
    amount=u*2
print("The electricity bill is rs.",amount)