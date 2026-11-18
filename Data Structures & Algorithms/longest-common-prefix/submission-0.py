class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        max_i = min(len(s) for s in strs)

        for i in range(max_i):
            c = strs[0][i]
            matches_all = True

            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    matches_all = False
                    break 

            if not matches_all:
                break

            res += c

        return res