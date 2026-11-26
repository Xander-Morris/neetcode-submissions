from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def _traverse(i, op):
            if i >= len(s):
                return op == 0
            
            if s[i] == '(':
                if len(s) - (op + 1) < 0:
                    return False 
                    
                return _traverse(i + 1, op + 1)
            elif s[i] == ')':
                if op <= 0:
                    return False

                return _traverse(i + 1, op - 1)
            else:
                trav = _traverse(i + 1, op) or _traverse(i + 1, op + 1)

                if op > 0:
                    trav = trav or _traverse(i + 1, op - 1)
                
                return trav 
            
        return _traverse(0, 0)