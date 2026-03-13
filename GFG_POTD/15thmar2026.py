# Given a binary tree, return an array of nodes visible from the top view from left to right.
from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        q = deque([(root, 0)])
        mp = {}
        
        while q:
            node, hd = q.popleft()
            
            if hd not in mp:
                mp[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        ans = []
        for k in sorted(mp):
            ans.append(mp[k])
        
        return ans