class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        mp = defaultdict(str)
        mp["2"] = {"a", "b", "c"}
        mp["3"] = {"d", "e", "f"}
        mp["4"] = {"g", "h", "i"}
        mp["5"] = {"j", "k", "l"}
        mp["6"] = {"m", "n", "o"}
        mp["7"] = {"p", "q", "r", "s"}
        mp["8"] = {"t", "u", "v"}
        mp["9"] = {"w", "x", "y", "z"}
        stack = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(stack))
                return

            for char in mp[digits[i]]:
                stack.append(char)
                backtrack(i + 1)
                stack.pop()

        backtrack(0)

        return res