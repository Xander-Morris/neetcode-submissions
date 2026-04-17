class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # Create an empty board filled with "."
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # If we reach the last row, then we have solved the problem.
            if r == n:
                # "".join(row) turns the row into a string for each row in the board.
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "." # Undo our decision to make it a queen.

        backtrack(0)

        return res

    def isSafe(self, r: int, c: int, board):
        row = r - 1

        # Checking previous rows in the same column. 
        while row >= 0:
            if board[row][c] == "Q":
                return False

            row -= 1

        # Checking diagonals to the left.
        row, col = r - 1, c - 1

        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False

            row -= 1
            col -= 1

        # Checking diagonals to the right.
        row, col = r - 1, c + 1

        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
                
            row -= 1
            col += 1

        return True