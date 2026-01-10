## Count of substrings with exactly K distinct characters
class Solution:
    def countSubstr(self, s, k):
        if k == 0:
            return 0
        
        def atMostK(s, k):
            freq = {}
            left = 0
            res = 0
            
            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1
                
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                
                # all substrings ending at `right` and starting from [left..right]
                res += right - left + 1
            
            return res
        
        return atMostK(s, k) - atMostK(s, k - 1)
