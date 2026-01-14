#candy-distribution-problem
class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        candies = [1] * n  # everyone gets at least 1
        
        # Left to right
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Right to left
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
