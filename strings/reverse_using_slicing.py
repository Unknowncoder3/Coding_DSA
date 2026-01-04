#Reverse the string using slicing.
n=str(input("Enter a string: "))
reversed_string=n[::-1]
print("Reversed string is:", reversed_string)
#reverse without slicing
reversed_string_no_slicing=""
for char in n:
    reversed_string_no_slicing=char+reversed_string_no_slicing
print("Reversed string without slicing is:", reversed_string_no_slicing)
