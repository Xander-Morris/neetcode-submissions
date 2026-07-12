class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = minutes_elapsed = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if fresh_fruits == 0:
            return 0 

        while q:
            minutes_elapsed += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for idelta, jdelta in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ni, nj = i + idelta, j + jdelta
                    if ni not in range(len(grid)) or nj not in range(len(grid[ni])):
                        continue
                    if grid[ni][nj] != 1:
                        continue
                    grid[ni][nj] = 2
                    fresh_fruits -= 1
                    if fresh_fruits <= 0:
                        return minutes_elapsed
                    q.append((ni, nj))

        return -1