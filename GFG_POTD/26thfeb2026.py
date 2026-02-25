# Given two strings s1 and s2, determine if they are isomorphic. Two strings are isomorphic if the characters in s1 can be replaced to get s2. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        m1, m2 = {}, {}
        
        for c1, c2 in zip(s1, s2):
            if c1 in m1 and m1[c1] != c2:
                return False
            if c2 in m2 and m2[c2] != c1:
                return False
            
            m1[c1] = c2
            m2[c2] = c1
        
        return True