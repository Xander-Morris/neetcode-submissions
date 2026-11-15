class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m = len(matrix)
        n = len(matrix[0])
        memo = {}

        def _traverse(r, c, visited):
            if r not in range(m) or c not in range(n):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            res = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr not in range(m) or nc not in range(n):
                    continue
                if matrix[nr][nc] - matrix[r][c] <= 0:
                    continue
                if (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                res = max(res, 1 + _traverse(nr, nc, visited))
                visited.remove((nr, nc))
            
            memo[(r, c)] = res 
            return res
        
        res = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                res = max(res, _traverse(r, c, set([(r, c)])))

        return res 