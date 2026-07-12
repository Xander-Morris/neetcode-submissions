class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0] # resulting substring
        
        def helper(i, j):
            nonlocal res
            sub = ""

            while i in range(n) and j in range(n):
                if s[i] != s[j]:
                    break
                if j - i + 1 > len(res):
                    res = s[i:j+1]
                i -= 1
                j += 1

        for i, char in enumerate(s):
            helper(i - 1, i + 1)
            helper(i, i + 1)

        return res