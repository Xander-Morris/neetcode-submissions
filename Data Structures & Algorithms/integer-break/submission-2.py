from functools import cache 

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache 
        def _traverse(n, k):
            if n == 0:
                return 1

            res = 0

            for i in range(n - max(k - 1, 0), 0, -1):
                res = max(res, i * _traverse(n - i, k - 1))
            
            return res 
            
        return _traverse(n, 2)