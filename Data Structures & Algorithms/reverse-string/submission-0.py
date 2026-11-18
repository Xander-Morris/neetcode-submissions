class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, h = 0, len(s) - 1

        while l < h:
            prev_l, prev_h = s[l], s[h]
            s[h] = prev_l
            s[l] = prev_h
            l += 1
            h -= 1