class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result = max(result, 1)
            seen = set()
            seen.add(s[i])

            for j in range(i + 1, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])

                result = max(result, j - i + 1)

        return result