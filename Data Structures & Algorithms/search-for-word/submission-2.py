class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # If the index in the word we are trying to match is equal to the
            # length of the word, then we have matched all the characters.
            if i == len(word):
                return True

            # min(r, c) is semantically the same as checking if either r or c
            # are < 0. It means if r < 0 or c < 0.
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            
            return res

        # Try to start the word at each cell position, and return true if
        # any of them are valid. 
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False