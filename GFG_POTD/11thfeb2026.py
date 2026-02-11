# Given two arrays heights and cost of size N, the task is to find the minimum cost to make all the heights equal. The cost of changing the height of the ith element is given by cost[i].
class Solution:
    def minCost(self, heights, cost):
        # Pair and sort by heights
        arr = sorted(zip(heights, cost))
        
        total_cost = sum(cost)
        half = total_cost // 2
        
        # Find weighted median
        curr = 0
        target = 0
        
        for h, c in arr:
            curr += c
            if curr > half:
                target = h
                break
        
        # Calculate final cost
        result = 0
        for h, c in arr:
            result += abs(h - target) * c
        
        return result
