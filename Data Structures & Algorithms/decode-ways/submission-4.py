class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n : 1} # allows endpoint for recursive dfs call without explicitly checking in dfs function

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            # this checks if the character can be the start of a 2-character number, like 15 or 26
            # if there is at least one character after this, and this current character is a 1 or a 2,
            # and the next character after this is in the range of 0-6,
            # then a two-character number can be formed since the range of numbers is 1 to 26 in this problem
            if i + 1 in range(n) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)