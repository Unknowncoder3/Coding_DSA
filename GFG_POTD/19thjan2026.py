# Remove K digits to form the smallest number
class Solution:
    def removeKdig(self, s, k):
        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If k still remains, remove from the end
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Build result and remove leading zeros
        res = ''.join(stack).lstrip('0')

        return res if res else "0"
