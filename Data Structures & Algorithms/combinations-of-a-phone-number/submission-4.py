class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []

        def dfs(comb, i):
            nonlocal res
            if i == len(digits):
                res.append("".join(comb))
                return
            
            for char in mp[digits[i]]:
                comb.append(char)
                dfs(comb, i + 1)
                comb.pop()
        
        dfs([], 0)

        return res