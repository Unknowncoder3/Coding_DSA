# Given a binary tree, return an array of vertical order traversal of the given tree.
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        hd_map = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            hd_map[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        for key in sorted(hd_map):
            result.append(hd_map[key])
        
        return result
