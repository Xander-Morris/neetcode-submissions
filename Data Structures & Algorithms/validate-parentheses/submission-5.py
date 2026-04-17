class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '[', '{']
        close = [')', ']', '}']
        open_stack = []

        for char in s:
            # If the character is an "open" character, then append it to the open_stack.
            if char in open:
                open_stack.append(char)
            else:
                # The character is a "close" character.
                # If there is no "open" character for it yet, then return false.
                if len(open_stack) <= 0:
                    return False

                top = open_stack[-1] # Take the last element.
                open_stack = open_stack[:-1] # Pop the last element.
                # Compare the indices of the "open" character and the "close" character
                # in their respective lists. Note that they are perfectly lined up in terms
                # of indices. 
                idx = open.index(top)

                # If the respective indices do not match, then we have the wrong closing character for the last opening character.
                if idx != close.index(char):
                    return False
        
        # All of the "open" characters have to be popped off of the stack for it to be valid.
        return len(open_stack) == 0