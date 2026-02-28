# Given two sorted arrays arr1 and arr2 of size N and M respectively, and a number X. The task is to find the pair whose sum is closest to X and return the pair in an array. If there are multiple pairs, return the pair with the smallest sum.
class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i, j = 0, len(arr2) - 1
        min_diff = float('inf')
        res = [0, 0]

        while i < len(arr1) and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)

            if diff < min_diff:
                min_diff = diff
                res = [arr1[i], arr2[j]]

            if curr_sum > x:
                j -= 1
            else:
                i += 1

        return res