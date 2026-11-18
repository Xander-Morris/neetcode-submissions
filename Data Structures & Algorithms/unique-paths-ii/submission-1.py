from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def _traverse(r, c):
            if obstacleGrid[r][c] == 1:
                return 0 # valid path cannot include obstacle
            if r == m - 1 and c == n - 1:
                return 1

            res = 0
            
            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc

                if nr not in range(m) or nc not in range(n):
                    continue
                
                res += _traverse(nr, nc)

            return res

        return _traverse(0, 0)