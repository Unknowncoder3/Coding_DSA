# Problem Statement: Given an array arr[] of size N representing the heights of people standing in a queue,
class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        L = [-1] * n
        R = [n] * n
        
        # Nearest >= on left
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Nearest >= on right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)
        
        ans = 0
        for i in range(n):
            visible = (i - L[i] - 1) + (R[i] - i - 1) + 1
            ans = max(ans, visible)
        
        return ans
