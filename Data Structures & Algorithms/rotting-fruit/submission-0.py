class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is an example of a problem where you have to fill the queue up
        # with nodes before you process them since they all contribute 
        # to the overall goal together, and we do not want to process one node before
        # processing the others.
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and q:
            length = len(q)

            # We want to pop all of them instead of just the top.
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
                        
            time += 1

        return time if fresh == 0 else -1