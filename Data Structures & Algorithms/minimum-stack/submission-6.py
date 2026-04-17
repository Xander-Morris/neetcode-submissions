class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        popped = self.stack.pop()

        if self.min == popped:
            self.min = float('inf')
            
            for val in self.stack:
                self.min = min(self.min, val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
