# Given an array of integers,find the length of the longest subarray that contains at most two distinct integers.s
class Solution:
    def totalElements(self, arr):
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        ans = 0
        
        for right in range(len(arr)):
            freq[arr[right]] += 1
            
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans