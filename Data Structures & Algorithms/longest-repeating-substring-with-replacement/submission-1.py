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

            # the window size - the max frequency of a character gives us
            # the number of replacements we would need to make
            # while that is greater than the max number of replacements we can
            # make (k), we must decrease the window size by decrementing the count
            # of the character pointed to by the left pointer
            # and increasing the left pointer by 1
            while getWindowSize() - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, getWindowSize())

        return res