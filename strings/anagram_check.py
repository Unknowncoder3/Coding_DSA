#anagram check of a string using function
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
# Example usage:
s1 = str(input("Enter first string: "))
s2 = str(input("Enter second string: "))
if are_anagrams(s1, s2):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are not anagrams.')
    