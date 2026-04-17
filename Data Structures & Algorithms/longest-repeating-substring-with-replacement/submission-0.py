class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            def getWindowSize():
                return (r - l) + 1

            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while getWindowSize() - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, getWindowSize())

        return res