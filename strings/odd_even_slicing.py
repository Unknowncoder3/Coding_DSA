#odd-even index slicing examples
n=str(input("Enter a string:"))
even_indexed_chars=n[::2]
odd_indexed_chars=n[1::2]
print("Characters at even indices:", even_indexed_chars)
print("Characters at odd indices:", odd_indexed_chars)
