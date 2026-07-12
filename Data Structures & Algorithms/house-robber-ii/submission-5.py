class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            """
                If we are farther than the array bounds, 
                or the first house was robbed and we are thinking of robbing the last house, 
                then return 0.
            """
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]

            """
                Maximum of skipping this house, or robbing it and moving on to the house two indices down.
                flag or (i == 0) just means that the flag is true if the flag was already set to be true, 
                or if the current index is 0   
            """ 
            memo[i][flag] = max(dfs(i + 1, flag),
                            nums[i] + dfs(i + 2, flag or (i == 0)))

            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))