class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    continue

                # It is crucial to remember that a new BFS starts the very moment
                # we see a member of the grid that we want to start a path from.
                # We do not collect the nodes and then traverse them later.
                grid[r][c] = 0 # Marking it as 0 to not be counted again. 
                count = 1 # Include the current node.
                q = deque()
                q.appendleft((r, c))

                while q:
                    row, col = q.popleft()

                    for direct in directions:
                        nr, nc = row + direct[0], col + direct[1]
                        
                        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[nr]):
                            continue
                        
                        if grid[nr][nc] == 0:
                            continue
                        
                        count += 1
                        grid[nr][nc] = 0
                        q.appendleft((nr, nc))

                res = max(res, count)
        
        return res