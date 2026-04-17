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

                # if there is a mismatch between the types of chars, then return false 
                if op_idx != close_idx:
                    return False
            else:
                # append the opening chars 
                stack.append(char)
        
        # only return true if all opening chars have been matched correctly 
        return len(stack) == 0