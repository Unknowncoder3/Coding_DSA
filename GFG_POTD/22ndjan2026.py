#Sum of subarray ranges
class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def getPrevNext(compare):
            prev = [-1] * n
            next = [n] * n
            stack = []

            for i in range(n):
                while stack and compare(arr[stack[-1]], arr[i]):
                    idx = stack.pop()
                    next[idx] = i
                prev[i] = stack[-1] if stack else -1
                stack.append(i)

            return prev, next

        # For maximums: pop while stack top < current
        pG, nG = getPrevNext(lambda a, b: a < b)

        # For minimums: pop while stack top > current
        pS, nS = getPrevNext(lambda a, b: a > b)

        sumMax = 0
        sumMin = 0

        for i in range(n):
            left = i - pG[i]
            right = nG[i] - i
            sumMax += arr[i] * left * right

            left = i - pS[i]
            right = nS[i] - i
            sumMin += arr[i] * left * right

        return sumMax - sumMin
