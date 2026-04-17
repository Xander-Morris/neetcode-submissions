class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # This is just an edge case to account for.
        if len(digits) == 0:
            return []

        res = []
        # Create a mapping from keypad digits to possible characters.
        mp = defaultdict(str)
        mp["2"] = {"a", "b", "c"}
        mp["3"] = {"d", "e", "f"}
        mp["4"] = {"g", "h", "i"}
        mp["5"] = {"j", "k", "l"}
        mp["6"] = {"m", "n", "o"}
        mp["7"] = {"p", "q", "r", "s"}
        mp["8"] = {"t", "u", "v"}
        mp["9"] = {"w", "x", "y", "z"}
        stack = [] # Create a stack array for string operations.

        def backtrack(i):
            # If i is now out of bounds, then we have a valid solution.
            if i == len(digits):
                # "".join(stack) creates a string from the "stack" array
                res.append("".join(stack))
                return

            # For each character, explore the possible solutions, and pop the
            # character off of the "stack" array afterwards. 
            # However, the typical backtracking call of backtracking again after
            # popping is not here since that would cause malformed answers.
            # This is not a subset problem where a string can have an empty 
            # character in any position. Hence, we do not want the possibility of
            # considering solutions that may potentially
            # not contain a character in a position.
            for char in mp[digits[i]]:
                stack.append(char)
                backtrack(i + 1)
                stack.pop()

        backtrack(0)

        return res