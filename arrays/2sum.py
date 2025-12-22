#Two Sum : Check if a pair with given sum exists in Array
#Problem Statement: Given an array of integers arr[] and an integer target.
#1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
#2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
def two_sum_exists(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return "YES"
        seen.add(num)
    return "NO" 
def two_sum_indices(arr, target):
    num_to_index = {}
    for index, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    return (-1, -1)
# Example usage:
arr = input("Enter the array elements separated by space: ").split()
arr = list(map(int, arr))
target = int(input("Enter the target sum: "))
print(two_sum_exists(arr, target))  # Output: "YES"
print(two_sum_indices(arr, target))  # Output: (0, 3)   