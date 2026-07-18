class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def backtrack(curr_grid, row, queens):
            if row == n:
                if queens < n:
                    return
                # create usable version for solution return (problem requires strings, not lists)
                res = []
                for r in range(len(curr_grid)):
                    res.append("".join(curr_grid[r]))
                solutions.append(res)
                return
            
            def _is_safe(row, col):
                # Check column and diagonals above
                for i in range(row):
                    if curr_grid[i][col] == 'Q':
                        return False
                    # Check upper-left diagonal
                    if col - (row - i) >= 0 and curr_grid[i][col - (row - i)] == 'Q':
                        return False
                    # Check upper-right diagonal
                    if col + (row - i) < n and curr_grid[i][col + (row - i)] == 'Q':
                        return False
                return True

            for col in range(n):
                if not _is_safe(row, col):
                    continue
                # backtrack 
                curr_grid[row][col] = 'Q'
                backtrack(curr_grid, row + 1, queens + 1)
                curr_grid[row][col] = '.'

        start_grid = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(start_grid, 0, 0)

        return solutions