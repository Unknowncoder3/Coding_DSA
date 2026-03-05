# Given two strings s and p, return the minimum window in s which will contain all the characters in p. If there is no such window in s that covers all characters in p, return the empty string "".
class Solution:
    def minWindow(self, s, p):
        from collections import Counter
        
        need = Counter(p)
        window = {}
        
        have = 0
        need_count = len(need)
        
        l = 0
        res = [-1, -1]
        res_len = float('inf')
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_count:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return "" if res_len == float('inf') else s[l:r+1]