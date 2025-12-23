#detecting double space in a string
n=str(input("Enter a string: "))
double_space_detected="  " in n
print("Does the string contain double spaces? :", double_space_detected)
output= n.replace("  "," ")
print("String after removing double spaces:", output)