#reverse a string without slicing
n=str(input("Enter a string: "))
reversed_string_no_slicing=""
for char in n:
    reversed_string_no_slicing=char+reversed_string_no_slicing
print("Reversed string without slicing is:", reversed_string_no_slicing)