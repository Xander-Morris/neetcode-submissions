from functools import cache 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache 
        def _traverse(amount):
            if amount == 0:
                return 0 
            
            res = float('inf')

            for coin in coins:
                if amount - coin < 0:
                    continue
                
                res = min(res, 1 + _traverse(amount - coin))

            return res

        res = _traverse(amount)

        return res if res != float('inf') else -1