#string length without using len() function
n=str(input("Enter a string: "))
count=0
for char in n:
    count+=1
print("Length of the string is:", count)