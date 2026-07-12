class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j) # dfs call that doesn't add on to the ILS length from previous number 

            if j == -1 or nums[j] < nums[i]:
                # if this new number is greater than the previous number, then we can possibly increase the calculated LIS
                # therefore, new LIS is maximum of itself and 1 + dfs(i + 1, i) 
                # meaning that we add 1 to the length of the ILS and then add the result of the dfs call where i + 1
                # is the new base index to compare, and i (the current index) is the PREVIOUS index to compare
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)