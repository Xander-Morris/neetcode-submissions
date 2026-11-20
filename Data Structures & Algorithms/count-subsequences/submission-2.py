from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def _traverse(i, j):
            if j == len(t):
                return 1
            
            res = 0

            for k in range(i, len(s)):
                if s[k] == t[j]:
                    res += _traverse(k + 1, j + 1)
                
            return res
        
        return _traverse(0, 0)