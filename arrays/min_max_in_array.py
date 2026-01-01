#minimum and maximum elements in an array
def min_max_in_array(arr):
    if not arr:
        return None, None
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum
array = [int(x) for x in input("Enter elements of the array separated by spaces: ").split()]
minimum, maximum = min_max_in_array(array)
if minimum is not None and maximum is not None:
    print(f"Minimum element is: {minimum}")
    print(f"Maximum element is: {maximum}")
else:
    print("The array is empty.")
