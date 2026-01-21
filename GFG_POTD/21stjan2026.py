# Function to calculate the stock span values
class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = []  # will store indices

        for i in range(n):
            # Pop elements while current price is greater or equal
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack empty, span is i+1
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push current index
            stack.append(i)

        return span
