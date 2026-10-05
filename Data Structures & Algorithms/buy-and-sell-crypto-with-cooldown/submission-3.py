class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        # total = current total, value = value of current neet coin we bought previously
        def _traverse(i, holding):
            if i >= len(prices):
                return 0 

            if (i, holding) in memo:
                return memo[(i, holding)]

            res = _traverse(i + 1, holding) # do nothing

            if holding:
                # prices[i] since we sell (sell = add)
                res = max(res, prices[i] + _traverse(i + 2, False)) # sell, then cooldown since we cannot buy on next day after selling
            else:
                # -prices[i] to buy (cost = subtraction)
                res = max(res, -prices[i] + _traverse(i + 1, True)) # buy

            memo[(i, holding)] = res
            return res

        return _traverse(0, False)