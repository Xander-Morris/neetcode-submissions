class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1 

        memo = {}

        def _traverse(i, left):
            if left <= 0:
                return 1 if left == 0 else 0

            if i in memo and left in memo[i]:
                return memo[i][left]
            
            res = 0

            for j in range(i, len(coins)):
                new_l = left - coins[j]
                
                if new_l < 0:
                    continue
                
                res += _traverse(j, new_l)
            
            if i not in memo:
                memo[i] = {}
                
            memo[i][left] = res

            return res

        res = 0

        for i in range(len(coins)):
            res += _traverse(i, amount - coins[i])

        return res