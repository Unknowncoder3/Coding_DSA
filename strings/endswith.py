#endswith examples
n=str(input("Enter a string: "))
end_substr=str(input("Enter the ending substring to check: "))
ends_with=n.endswith(end_substr)
print(f"Does the string end with '{end_substr}'? :", ends_with)