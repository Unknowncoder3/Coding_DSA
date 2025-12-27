#Binary search using user defines function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example usage
arr = list(map(int, input("Enter sorted elements of the array separated by spaces: ").split()))
target = int(input("Enter the target element to search for: "))
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
