# Problem Statement: Given a string s consisting of lowercase English letters, you need to find the first non-repeating character in the stream of characters formed by the string s at each point in time. If there is no such character, append '#' to the result.
from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26
        q = deque()
        ans = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            if q:
                ans.append(q[0])
            else:
                ans.append('#')

        return "".join(ans)
