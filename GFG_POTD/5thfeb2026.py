# Given a binary array arr[] of size N and an integer K, find the maximum number of consecutive 1's in the array if you can flip at most K 0's.
class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(arr)):
            # If we see a zero, increase zero count
            if arr[right] == 0:
                zero_count += 1

            # If zeros exceed k, shrink from left
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum window size
            max_len = max(max_len, right - left + 1)

        return max_len
