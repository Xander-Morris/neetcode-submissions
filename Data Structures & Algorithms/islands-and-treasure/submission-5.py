class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        def _add_cell(r, c):
            if r not in range(len(grid)) or c not in range(len(grid[r])):
                return
            if (r, c) in visited:
                return
            if grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))

        # add all treasure spots to initial queue for bfs
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    continue
                _add_cell(i, j)
        
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level 
                _add_cell(r + 1, c)
                _add_cell(r - 1, c)
                _add_cell(r, c + 1)
                _add_cell(r, c - 1)
            level += 1