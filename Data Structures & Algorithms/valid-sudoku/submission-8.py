class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9

        def checkRowOrCol(is_row : bool):
            for i in range(length):
                seen = set()
                for j in range(length):
                    val = board[i][j] if is_row else board[j][i]
                    
                    if val == ".":
                        continue

                    if val in seen:
                        return False 
                    
                    seen.add(val)

            return True
        
        if not checkRowOrCol(True) or not checkRowOrCol(False):
            return False
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True