# Given an array of non-negative integers, arrange them such that they form the largest number and return it as a string.
class Solution:
    def findLargest(self, arr):
        from functools import cmp_to_key
        
        # Convert integers to strings
        arr = list(map(str, arr))
        
        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Edge case: if largest number is "0"
        if arr[0] == "0":
            return "0"
        
        return "".join(arr)
