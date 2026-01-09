# Problem Statement: Given an array of integers and an integer K, find the number of subarrays with at most K distinct integers.
class Solution:
    def countAtMostK(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(arr)):
            freq[arr[right]] += 1
            
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            result += (right - left + 1)
        
        return result