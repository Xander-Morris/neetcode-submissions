class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # order of operations matters for - and /
        for c in tokens:
            print(stack)
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
            print(stack)
                
        return stack[0] # remaining element has answer 