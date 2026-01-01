#finding the k-th element in an array
def kth_element(arr, k):
    if k < 1 or k > len(arr):
        return None
    return arr[k - 1]
array = [int(x) for x in input("Enter elements of the array separated by spaces: ").split()]
k = int(input("Enter the value of k: "))
result = kth_element(array, k)
if result is not None:
    print(f"The {k}-th element is: {result}")
else:
    print("Invalid value of k")