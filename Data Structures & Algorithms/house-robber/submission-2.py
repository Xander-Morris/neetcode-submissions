class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def dfs(i):
            if i not in range(n):
                return 0 
            if i in dp:
                return dp[i]
            
            """
                in English, this expression means the following:
                take the maximum result from one of the following actions we can take: 
                1. rob this house, and then rob the house two houses away to start robbing again
                2. skip robbing this house entirely, and just start robbing from the next house
            """
            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return dp[i]

        return dfs(0)