class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for c in range(len(matrix[0])):
            new_row = [matrix[r][c] for r in range(len(matrix))]
            res.append(new_row)

        return res