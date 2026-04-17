class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == len(t):
            return s == t
        if len(s) == 0:
            return True
        
        for i in range(len(t) - len(s)):
            if t[i] != s[0]:
                continue
            
            # starting point has been found
            matching = 1
            j = i + 1

            while j < len(t) and matching < len(s):
                if t[j] != s[matching]:
                    j += 1
                    continue
                
                matching += 1
                j += 1
            
            if matching >= len(s):
                return True

        return False