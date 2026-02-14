# Given an array of integers arr and an integer m, find the minimum difference between the maximum and minimum of any m elements in the array.
class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        # Edge case
        if m == 0 or n == 0:
            return 0
        
        if m > n:
            return -1
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize result with large value
        min_diff = float('inf')
        
        # Step 3: Check every window of size m
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff