class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def _traverse(i, j):
            if i not in range(len(text1)) or j not in range(len(text2)):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
                        
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + _traverse(i + 1, j + 1)
            else:
                memo[(i, j)] = max(_traverse(i + 1, j), _traverse(i, j + 1))

            return memo[(i, j)]

        return _traverse(0, 0)