# average of numbers
n=int(input("Enter how many numbers you want to average: "))
total=0
for i in range(n):
    num=float(input(f"Enter number {i+1}: "))
    total+=num
average=total/n
print("The average of the entered numbers is:", average)