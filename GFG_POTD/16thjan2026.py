#Minimum Number of Workers
class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        for i in range(n):
            if arr[i] != -1:
                l = max(0, i - arr[i])
                r = min(n - 1, i + arr[i])
                intervals.append((l, r))
        
        # Sort by start
        intervals.sort()
        
        cnt = 0
        pos = 0
        i = 0
        m = len(intervals)
        
        while pos < n:
            farthest = pos
            
            # Take all intervals that start <= pos
            while i < m and intervals[i][0] <= pos:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1
            
            # If we couldn't extend coverage
            if farthest == pos:
                return -1
            
            cnt += 1
            pos = farthest
        
        return cnt
