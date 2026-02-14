# Given an array of integers arr and an integer k, where arr[i] represents the length of the ith board, and k represents the number of painters available. Each painter can paint 1 unit of board in 1 unit of time. The task is to find the minimum time required to paint all the boards.
class Solution:
    def minTime(self, arr, k):
        def isPossible(max_time):
            painters = 1
            curr_sum = 0
            
            for length in arr:
                if curr_sum + length <= max_time:
                    curr_sum += length
                else:
                    painters += 1
                    curr_sum = length
                    if painters > k:
                        return False
            return True
        
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans