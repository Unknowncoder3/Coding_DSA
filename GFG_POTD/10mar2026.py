# Given an array of integers, count the number of subarrays where the minimum element is the first element of the subarray.
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            ans += next_smaller[i] - i

        return ans