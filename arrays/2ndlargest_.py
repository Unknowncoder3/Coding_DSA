#Find the largest and second largest element in an array
def second_largest_in_array(arr):
    if len(arr) < 2:
        return None, None
    first = second = float('-inf')
    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    if second == float('-inf'):
        return first, None
    return first, second
array = [int(x) for x in input("Enter elements of the array separated by spaces: ").split()]
largest, second_largest = second_largest_in_array(array)
if largest is not None:
    print(f"Largest element is: {largest}")
    if second_largest is not None:
        print(f"Second largest element is: {second_largest}")
    else:
        print("There is no second largest element.")
else:
    print("The array does not have enough elements.")
