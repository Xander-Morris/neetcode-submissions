class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            seen_zeros = []

            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                
                seen_zeros.append(j)

            for j in seen_zeros:
                for ii in range(len(matrix)):
                    if matrix[ii][j] == 0:
                        continue
                    matrix[ii][j] = -1
                
                for jj in range(len(matrix[i])):
                    if matrix[i][jj] == 0:
                        continue
                    matrix[i][jj] = -1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

    
        