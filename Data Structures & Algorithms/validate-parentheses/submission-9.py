class Solution:
    def isValid(self, s: str) -> bool:
        op_chars = ['(', '[', '{']
        close_chars = [')', ']', '}']
        stack = []

        for char in s:
            if char in close_chars:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                op_idx = op_chars.index(top)
                close_idx = close_chars.index(char)

                if op_idx != close_idx:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0