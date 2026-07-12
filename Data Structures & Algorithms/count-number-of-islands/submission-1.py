class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '1':
                    continue
                # start of island, so start bfs
                res += 1
                pq = [(i, j)]
                grid[i][j] = '0'

                while pq:
                    for _ in range(len(pq)):
                        r, c = heapq.heappop(pq)

                        for rdelta, cdelta in dirs:
                            nr = r + rdelta
                            nc = c + cdelta
                            if nr not in range(len(grid)) or nc not in range(len(grid[nr])):
                                continue
                            if grid[nr][nc] != '1':
                                continue
                            grid[nr][nc] = '0'
                            heapq.heappush(pq, (nr, nc))

        return res