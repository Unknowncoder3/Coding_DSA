# Given two arrays a1 and a2 of equal length n, find the length of the longest span (i, j) such that the sum of elements from i to j is the same in both arrays.
class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        
        diff_index = {}
        prefix_diff = 0
        max_len = 0
        
        for i in range(n):
            prefix_diff += a1[i] - a2[i]
            
            if prefix_diff == 0:
                max_len = i + 1
            elif prefix_diff in diff_index:
                max_len = max(max_len, i - diff_index[prefix_diff])
            else:
                diff_index[prefix_diff] = i
        
        return max_len