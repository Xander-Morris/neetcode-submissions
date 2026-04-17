class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '[', '{']
        close = [')', ']', '}']
        open_stack = []

        for char in s:
            if char in open:
                open_stack.append(char)
            else:
                if len(open_stack) <= 0:
                    return False
                    
                top = open_stack[-1]
                open_stack = open_stack[:-1]
                idx = open.index(top)

                if idx != close.index(char):
                    return False
        
        return len(open_stack) == 0