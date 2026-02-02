# Problem Statement: Given a circular array, find the maximum sum of a subarray.
class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)

        # Standard Kadane to find max subarray sum
        max_end = arr[0]
        max_so_far = arr[0]

        # Kadane to find min subarray sum
        min_end = arr[0]
        min_so_far = arr[0]

        total = arr[0]

        for i in range(1, n):
            # Max subarray sum
            max_end = max(arr[i], max_end + arr[i])
            max_so_far = max(max_so_far, max_end)

            # Min subarray sum
            min_end = min(arr[i], min_end + arr[i])
            min_so_far = min(min_so_far, min_end)

            total += arr[i]

        # If all elements are negative
        if max_so_far < 0:
            return max_so_far

        # Maximum of normal and circular case
        return max(max_so_far, total - min_so_far)
