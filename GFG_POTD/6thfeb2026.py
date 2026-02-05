#Happiest Triplet

class Solution:
    def smallestDiff(self, a, b, c):

        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0

        best_diff = float('inf')
        best_sum = float('inf')
        ans = []

        while i < len(a) and j < len(b) and k < len(c):

            x, y, z = a[i], b[j], c[k]

            mx = max(x, y, z)
            mn = min(x, y, z)

            diff = mx - mn
            s = x + y + z

            # Update answer
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                ans = [x, y, z]

            # Move pointer of minimum element
            if mn == x:
                i += 1
            elif mn == y:
                j += 1
            else:
                k += 1

        # return in decreasing order
        ans.sort(reverse=True)
        return ans
