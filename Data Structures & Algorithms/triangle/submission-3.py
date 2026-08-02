class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle[row]) for row in range(len(triangle))]
        dp[-1] = triangle[-1][:]

        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[r][c] = triangle[r][c] + min(dp[r + 1][c], dp[r + 1][c + 1])

        return dp[0][0]