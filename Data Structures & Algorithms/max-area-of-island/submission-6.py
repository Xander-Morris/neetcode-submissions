class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 # max area of island found 
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 1:
                    continue
                # start bfs from here
                nodes_connected = 1
                # can still set to 0 in problems like these, no need for visited set
                # reason why is because you would get max area of island no matter which "1" you started from
                # so avoiding setting it to 0 is not necessary 
                grid[i][j] = 0
                pq = [(i, j)]

                while pq:
                    for _ in range(len(pq)):
                        r, c = heapq.heappop(pq)
                        
                        for rdelta, cdelta in dirs:
                            nr = r + rdelta
                            nc = c + cdelta

                            if nr not in range(len(grid)) or nc not in range(len(grid[nr])):
                                continue
                            if grid[nr][nc] != 1:
                                continue
                            nodes_connected += 1
                            grid[nr][nc] = 0
                            heapq.heappush(pq, (nr, nc))
                
                res = max(res, nodes_connected)

        return res