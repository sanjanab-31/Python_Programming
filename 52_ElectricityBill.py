u=float(input("Enter the units consumed: "))
if u<=100:
    print("Electricity bill: ",u*5)
elif u<=200:
    print("Electricity bill: ",100*5+(u-100)*7)
elif u<=300:
    print("Electricity bill: ",100*5+100*7+(u-200)*10)
else:
    print("Electricity bill: ",100*5+100*7+100*10+(u-300)*15)