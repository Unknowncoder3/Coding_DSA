# Problem: Minimum Window Subsequence
class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        best_len = float('inf')
        best_start = -1
        
        i = 0
        while i < n:
            # Forward match
            j = 0
            k = i
            while k < n:
                if s1[k] == s2[j]:
                    j += 1
                    if j == m:
                        break
                k += 1
            
            if j < m:
                break
            
            end = k
            
            # Backward shrink
            j = m - 1
            while k >= i:
                if s1[k] == s2[j]:
                    j -= 1
                    if j < 0:
                        break
                k -= 1
            
            start = k
            
            # Update answer
            if end - start + 1 < best_len:
                best_len = end - start + 1
                best_start = start
            
            # Move i only one step ahead of the original start
            i = start + 1
        
        if best_start == -1:
            return ""
        
        return s1[best_start: best_start + best_len]
