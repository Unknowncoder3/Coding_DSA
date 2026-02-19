# Given an array of integers arr and two integers low and high, find the missing numbers in the range [low, high] that are not present in the array.
class Solution:
    def missingRange(self, arr, low, high):
        s = set(arr)
        result = []
        
        for x in range(low, high + 1):
            if x not in s:
                result.append(x)
                
        return result
