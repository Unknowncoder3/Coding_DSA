# Given an array of integers, find the maximum value of the sum of i*arr[i] for all i from 0 to n-1, where n is the size of the array. You can rotate the array any number of times.
class Solution:
    def maxSum(self, arr):
        n = len(arr)

        arr_sum = sum(arr)

        # Calculate initial configuration value R0
        curr_val = sum(i * arr[i] for i in range(n))

        max_val = curr_val

        # Compute next rotations using formula
        for i in range(1, n):
            curr_val = curr_val + arr_sum - n * arr[n - i]
            max_val = max(max_val, curr_val)

        return max_val
