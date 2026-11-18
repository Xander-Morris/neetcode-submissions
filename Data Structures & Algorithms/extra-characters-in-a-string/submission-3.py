from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        min_len = min(len(s) for s in words)
        max_len = max(len(s) for s in words)

        @cache 
        def _traverse(i):
            if i == len(s):
                return 0 

            res = float('inf')
            
            for t in range(i, len(s)):
                for length in range(min_len, max_len + 1):
                    j = t + length

                    if j > len(s):
                        continue
                    
                    # :j means not including character at index j
                    if s[t:j] not in words:
                        continue
                    
                    res = min(res, t - i + _traverse(j))
            
            return res if res != float('inf') else len(s) - i
        
        return _traverse(0)