class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n # each character is its own palindrome by problem definition 

        def _do_palindromes_check(l, r):
            nonlocal res

            while l in range(n) and r in range(n):
                if s[l] != s[r]:
                    # characters are no longer matching, so no longer a valid palindrome
                    break
                res += 1 # increment number of palindromic substrings to return as result 
                # move pointers 
                l -= 1
                r += 1

        for i in range(n):
            # use this index as center, and expand outward
            # both even and odd length palindromes must be accounted for 
            _do_palindromes_check(i - 1, i + 1) # odd length palindromes
            _do_palindromes_check(i, i + 1) # even length palindromes

        return res