#Triangle validity checker
a=int(input("Enter first side of triangle: "))
b=int(input("Enter second side of triangle: "))
c=int(input("Enter third side of triangle: "))
if a+b>c and b+c>a and c+a>b:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")