# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
import math

class Solution:
    def kokoEat(self, arr, k):
        low = 1
        high = max(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Calculate hours needed at speed mid
            hours = 0
            for p in arr:
                hours += math.ceil(p / mid)

            if hours <= k:
                ans = mid
                high = mid - 1   # try smaller speed
            else:
                low = mid + 1    # need more speed

        return ans
