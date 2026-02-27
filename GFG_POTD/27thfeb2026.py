# Given a 2D matrix of integers and an integer x, the task is to count the number of square submatrices that have a sum equal to x.
class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Build prefix sum matrix
        ps = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                ps[i][j] = mat[i][j]
                if i > 0:
                    ps[i][j] += ps[i-1][j]
                if j > 0:
                    ps[i][j] += ps[i][j-1]
                if i > 0 and j > 0:
                    ps[i][j] -= ps[i-1][j-1]
        
        count = 0
        
        # Try all square sizes
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    r = i + size - 1
                    c = j + size - 1
                    
                    total = ps[r][c]
                    if i > 0:
                        total -= ps[i-1][c]
                    if j > 0:
                        total -= ps[r][j-1]
                    if i > 0 and j > 0:
                        total += ps[i-1][j-1]
                    
                    if total == x:
                        count += 1
        
        return count