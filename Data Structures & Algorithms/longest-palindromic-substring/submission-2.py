class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def traverse(l, r):
            nonlocal res
            nonlocal resLen

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length
            l, r = i, i
            traverse(l, r)

            # even length
            l, r = i, i + 1
            traverse(l, r)

        return res