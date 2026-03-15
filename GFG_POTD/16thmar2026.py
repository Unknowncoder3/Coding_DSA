# Given a binary tree and an integer K, find the number of paths in the tree that sum up to K. A path can start from any node and end at any node in the tree, but it must go downwards (traveling only from parent nodes to child nodes).
class Solution:
    def countAllPaths(self, root, k):
        prefix = {0: 1}
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.data
            
            count = prefix.get(curr_sum - k, 0)
            
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)