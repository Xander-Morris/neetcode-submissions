class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)

            if prices[l] > prices[r]:
                # We have a new low point, so it is the most strategic decision to
                # start selling from here instead.
                l = r
            else:
                r += 1
        
        return res