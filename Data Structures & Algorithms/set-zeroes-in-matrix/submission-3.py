class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seen_zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                
                seen_zeros.append((i, j))

        for i, j in seen_zeros:
            for ii in range(len(matrix)):
                matrix[ii][j] = 0
            
            for jj in range(len(matrix[i])):
                matrix[i][jj] = 0
    
        