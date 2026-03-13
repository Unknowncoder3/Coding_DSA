# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
class Solution:
    def generateIp(self, s):
        res = []
        n = len(s)

        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    res.append(".".join(path))
                return

            for l in range(1, 4):
                if start + l > n:
                    break

                part = s[start:start+l]

                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(start+l, path + [part])

        backtrack(0, [])
        return res