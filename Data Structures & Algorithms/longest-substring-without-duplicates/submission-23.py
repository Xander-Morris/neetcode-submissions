class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        l = 0
        r = 0

        while r < len(s):
            while s[r] in chars:
                char = s[l]
                chars.remove(char)
                l += 1
            
            res = max(res, r - l + 1)
            chars.add(s[r])
            r += 1
        
        return res