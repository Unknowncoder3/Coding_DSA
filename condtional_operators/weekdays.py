#weekdays using chain of conditions
day=int(input("Enter a number (1-7) to get the corresponding weekday: "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")