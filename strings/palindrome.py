#palindrome check
s=str(input("Enter a string: "))
reversed_string=s[::-1]
if s==reversed_string:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")