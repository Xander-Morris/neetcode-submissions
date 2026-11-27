class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def _is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True 

        def _get_palindrome_ends(l):
            ends = []

            for r in range(l, len(s)):
                if _is_palindrome(l, r):
                    ends.append(r)

            return ends 

        res = []

        def _traverse(l, sub):
            if l >= len(s):
                res.append(sub[:])
                return
            
            ends = _get_palindrome_ends(l)

            for end in ends:
                sub.append(s[l:end+1])
                _traverse(end + 1, sub)
                sub.pop()

        _traverse(0, [])

        return res