class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for inner_mat in matrix:
            low = 0
            high = len(inner_mat) - 1

            while low <= high:
                middle = (low + high) // 2

                if inner_mat[middle] == target:
                    return True
                elif inner_mat[middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1

        return False