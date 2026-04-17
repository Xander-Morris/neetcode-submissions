class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == len(t):
            return s == t
        if len(s) == 0:
            return True
        
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            
            j += 1
        
        return i == len(s)