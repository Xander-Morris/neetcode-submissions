class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_part = True
        i = j = 0
        res = ""

        while i < len(word1) and j < len(word2):
            if word1_part:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1

            word1_part = not word1_part

        return res + word1[i:] + word2[j:]