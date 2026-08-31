class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def _dfs(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            
            res = _dfs(i + 1, bought)

            if bought:
                res = max(res, prices[i] + _dfs(i + 1, not bought))
            else:
                res = max(res, -prices[i] + _dfs(i + 1, True))
            
            dp[(i, bought)] = res

            return res

        return _dfs(0, False)