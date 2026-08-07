class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_cols = set()
        zero_rows = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                
                zero_cols.add(j)
                zero_rows.add(i)

        for c in zero_cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0

        for r in zero_rows:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
        