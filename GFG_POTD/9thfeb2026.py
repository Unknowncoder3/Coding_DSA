# Given a sorted and rotated array, find the number of times it has been rotated. The rotation count is the index of the minimum element in the array.
class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low, high = 0, n - 1

        # If already sorted, no rotation
        if arr[low] <= arr[high]:
            return 0

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is minimum
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return mid
            if mid < n - 1 and arr[mid] > arr[mid + 1]:
                return mid + 1

            # Decide which half to go
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1

        return 0
