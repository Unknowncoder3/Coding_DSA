# Given a binary array arr[] of size N and an integer K, the task is to find the minimum number of K-bit flips required to convert all the elements of the array to 1. If it is not possible, return -1.
class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = 0
        ans = 0
        isFlipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flip ^= isFlipped[i - k]
            
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                ans += 1
                flip ^= 1
                isFlipped[i] = 1
        
        return ans