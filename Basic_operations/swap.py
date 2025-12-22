#swap of two number using third variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
temp=a
a=b
b=temp
print("After swapping, first number is:", a)
print("After swapping, second number is:", b)