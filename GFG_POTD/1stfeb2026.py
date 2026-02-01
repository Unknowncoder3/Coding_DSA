# Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        res = []
        
        for i in range(len(arr)):
            # Remove elements out of this window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove smaller elements from the back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            dq.append(i)
            
            # First window completed
            if i >= k - 1:
                res.append(arr[dq[0]])
        
        return res
