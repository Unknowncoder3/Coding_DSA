#Last Moment Before All Ants Fall Out
class Solution:
    def getLastMoment(self, n, left, right):
        # Time for left-moving ants
        left_time = max(left) if left else 0
        
        # Time for right-moving ants
        right_time = max(n - x for x in right) if right else 0
        
        # Last moment any ant falls
        return max(left_time, right_time)
