#count vowels in a string
def count_vowels(s):
    return sum(1 for ch in s if ch in 'aeiouAEIOU')
# Example usage:
s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
