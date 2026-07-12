class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit:
                return
            if r not in range(ROWS) or c not in range(COLS):
                return 
            # we are actually starting from the outskirts of the graph and going inward, 
            # so the condition we check for is REVERSED from what the problem statement says 
            if heights[r][c] < prevHeight:
                return
                
            visit.add((r, c))
            # visit in all four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # all elements on first row are connected to pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # all elements on last row are connected to atlantic

        for r in range(ROWS):
            # all elements in column 0 are connected to pacific (the ones on the far-left of graph)
            dfs(r, 0, pac, heights[r][0]) 
            # all elements in the last column are connected to atlantic (the ones on far-right of graph)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res