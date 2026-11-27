class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        first_i = {}
        last_i = {}
        l = r = 0

        for i, c in enumerate(s):
            if c not in first_i:
                first_i[c] = i 
            last_i[c] = i

        curr_window_last_i = last_i[s[0]]

        while r < len(s):
            if r >= curr_window_last_i:
                res.append(r - l + 1)
                r += 1
                if r <= len(s) - 1:
                    curr_window_last_i = last_i[s[r]]
                l = r
                continue

            curr_window_last_i = max(curr_window_last_i, last_i[s[r]])
            r += 1

        return res