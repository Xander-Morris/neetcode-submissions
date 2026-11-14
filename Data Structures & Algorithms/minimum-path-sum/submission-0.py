from functools import cache 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        @cache
        def _traverse(i, j):
            if i not in range(m) or j not in range(n):
                return float('inf') 
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            return grid[i][j] + min(_traverse(i + 1, j), _traverse(i, j + 1))
        
        return _traverse(0, 0)