b=int(input("Enter base salary:"))
if(b<1000):
  da=0.25*b
  hra=0.3*b
  pf=0.08*b
  netsalary=b+da+hra-pf
  print(f"Basesalary={b}")
  print(f"DA={da}")
  print(f"HRA={hra}")
  print(f"PF={pf}")
  print(f"Netsalary={netsalary}")
else:
  da=0.2*b
  hra=0.25*b
  pf=0.06*b
  netsalary=b+da+hra-pf
  print(f"Basesalary={b}")
  print(f"DA={da}")
  print(f"HRA={hra}")
  print(f"PF={pf}")
  print(f"Netsalary={netsalary}")
        
