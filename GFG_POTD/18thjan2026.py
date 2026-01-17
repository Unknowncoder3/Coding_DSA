#Next element with greater frequency
class Solution:
    def nextFreqGreater(self, arr):
        from collections import Counter
        
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []  # will store indices
        
        for i in range(n):
            # Compare frequencies, not values
            while stack and freq[arr[i]] > freq[arr[stack[-1]]]:
                idx = stack.pop()
                res[idx] = arr[i]
            stack.append(i)
        
        return res
