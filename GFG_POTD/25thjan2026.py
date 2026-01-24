# Problem Statement: Given an integer n, find the number of ways to form balanced parentheses using n pairs of parentheses.
class Solution:
    def findWays(self, n):
        if n % 2 == 1:
            return 0
        
        k = n // 2
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(1, k + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        return dp[k]
