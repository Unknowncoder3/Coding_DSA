# Given two integers n and d, the task is to find the count of numbers from 1 to n such that the difference between the number and the sum of its digits is greater than or equal to d.
class Solution:
    def getCount(self, n, d):
        
        def digit_sum(x):
            return sum(int(c) for c in str(x))
        
        low, high = 1, n
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if mid - digit_sum(mid) >= d:
                ans = mid
                high = mid - 1   # try to find smaller valid
            else:
                low = mid + 1
        
        if ans == -1:
            return 0
        
        return n - ans + 1