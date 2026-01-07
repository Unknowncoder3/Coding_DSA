# Count subarrays with exactly K odd numbers

class Solution:
    def countSubarrays(self, arr, k):
        
        def atMost(k):
            left = 0
            odd_count = 0
            res = 0
            
            for right in range(len(arr)):
                if arr[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if arr[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                res += (right - left + 1)
            
            return res
        
        return atMost(k) - atMost(k - 1)
