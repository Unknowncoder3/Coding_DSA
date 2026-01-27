#Count Subset With Target Sum II

from bisect import bisect_left, bisect_right

class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        def gen_sums(a):
            sums = []
            def dfs(i, curr):
                if i == len(a):
                    sums.append(curr)
                    return
                dfs(i + 1, curr)
                dfs(i + 1, curr + a[i])
            dfs(0, 0)
            return sums
        
        left_sums = gen_sums(left)
        right_sums = gen_sums(right)
        
        right_sums.sort()
        ans = 0
        
        for s in left_sums:
            need = k - s
            ans += bisect_right(right_sums, need) - bisect_left(right_sums, need)
        
        return ans
