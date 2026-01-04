#palindrome check using function
def is_palindrome(s):
    reversed_string=s[::-1]
    return s==reversed_string
# Example usage:
s=str(input("Enter a string: "))
if is_palindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")