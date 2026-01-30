# Rearrange a Queue in specific order
from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q) // 2
        temp = deque()
        
        # Step 1: Move first half into temp queue
        for _ in range(n):
            temp.append(q.popleft())
        
        # Step 2: Interleave elements
        while temp:
            q.append(temp.popleft())  # from first half
            q.append(q.popleft())     # from second half
        
        return q
