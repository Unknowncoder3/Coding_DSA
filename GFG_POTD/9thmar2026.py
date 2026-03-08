# Given a string s of length n, consisting of digits from 0 to 9, you are allowed to swap two digits at most once. Your task is to find the largest possible number that can be obtained by performing at most one swap operation on the digits of the string.
class Solution:
    def largestSwap(self, s):
        arr = list(s)
        n = len(arr)

        # Store last occurrence of each digit
        last = {int(arr[i]): i for i in range(n)}

        for i in range(n):
            for d in range(9, int(arr[i]), -1):
                if d in last and last[d] > i:
                    arr[i], arr[last[d]] = arr[last[d]], arr[i]
                    return "".join(arr)

        return s