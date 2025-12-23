#concatenate two strings without using function
str1=str(input("Enter first string: "))
str2=str(input("Enter second string: "))
concatenated_string=""
for char in str1:
    concatenated_string+=char
for char in str2:
    concatenated_string+=char
print("Concatenated string is:", concatenated_string)
