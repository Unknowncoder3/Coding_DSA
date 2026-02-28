# Given an array of integers, move all the 0's to the end of the array while maintaining the relative order of the non-zero elements. The function should modify the input array in-place and return it.
class Solution:
    def pushZerosToEnd(self, arr):
        pos = 0  # position to place the next non-zero element

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1