import math 
from functools import cache 

class Solution:
    def numSquares(self, n: int) -> int:
        # n <= 10,000
        perfect_squares = [i * i for i in range(1, int(math.sqrt(10000)) + 1)]

        @cache 
        def _traverse(sum_left):
            if sum_left == 0:
                return 0 
            
            res = float('inf')

            for i in range(len(perfect_squares) - 1, -1, -1):
                num = perfect_squares[i]

                if sum_left - num < 0:
                    continue 
                
                res = min(res, 1 + _traverse(sum_left - num))

            return res  
        
        return _traverse(n)