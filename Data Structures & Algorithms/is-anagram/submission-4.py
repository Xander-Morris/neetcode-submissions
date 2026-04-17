class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = Counter(s)
        t_chars = Counter(t)

        for char in s_chars:
            if not char in t_chars or t_chars[char] < s_chars[char]:
                return False
        
        for char in t_chars:
            if not char in s_chars or s_chars[char] < t_chars[char]:
                return False

        return True