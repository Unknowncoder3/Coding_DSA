#Electricity bill calculation
units=int(input("Enter the number of electricity units consumed: "))
if units<=100:
    bill=units*5
elif units<=200:
    bill=100*5 + (units-100)*7
else:
    bill=100*5 + 100*7 + (units-200)*10
print("The total electricity bill is:", bill)