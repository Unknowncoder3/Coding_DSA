# Given an array of integers representing the height of bars, find the maximum amount of water that can be trapped between the bars after raining.
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water