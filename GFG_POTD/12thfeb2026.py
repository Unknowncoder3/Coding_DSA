# Given an array of integers arr, an integer k, and an integer w, you can perform the following operation at most k times:
class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def canReach(target):
            ops = 0
            add = [0] * (n + 1)   # difference array
            curr = 0

            for i in range(n):
                curr += add[i]

                if arr[i] + curr < target:
                    need = target - (arr[i] + curr)
                    ops += need

                    if ops > k:
                        return False

                    curr += need
                    if i + w < n:
                        add[i + w] -= need

            return True

        # Binary search on answer
        low = min(arr)
        high = min(arr) + k
        ans = low

        while low <= high:
            mid = (low + high) // 2

            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
