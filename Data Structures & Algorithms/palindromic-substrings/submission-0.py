class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s) # each character is its own palindrome by problem definition 

        def _do_palindromes_check(l, r):
            nonlocal res

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # use this index as center, and expand outward
            # both even and odd length palindromes must be accounted for 
            _do_palindromes_check(i - 1, i + 1)
            _do_palindromes_check(i, i + 1)

        return res