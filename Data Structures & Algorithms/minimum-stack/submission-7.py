class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:            
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return

        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return

        return self.min_stack[-1]
