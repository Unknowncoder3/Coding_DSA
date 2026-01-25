# Python3 code to find all distinct permutations of an array
# containing duplicates using backtracking
class Solution:
    def permuteDist(self, arr):
        res = []
        
        def backtrack(idx):
            if idx == len(arr):
                res.append(arr[:])
                return
            
            for i in range(idx, len(arr)):
                arr[idx], arr[i] = arr[i], arr[idx]
                backtrack(idx + 1)
                arr[idx], arr[i] = arr[i], arr[idx]  # backtrack
        
        backtrack(0)
        return res
