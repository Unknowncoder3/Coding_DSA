# Given an array of integers arr and an integer k, return the length of the longest subarray where the number of elements greater than k is strictly more than the number of elements less than or equal to k.
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        
        # Step 1: Convert array to +1 / -1
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if arr[i] > k else -1)
        
        # Step 2: Build decreasing stack of prefix indices
        stack = []
        for i in range(n + 1):
            if not stack or pref[i] < pref[stack[-1]]:
                stack.append(i)
        
        # Step 3: Traverse from right to left to find max length
        ans = 0
        for i in range(n, -1, -1):
            while stack and pref[i] > pref[stack[-1]]:
                ans = max(ans, i - stack[-1])
                stack.pop()
        
        return ans