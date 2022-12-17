class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minval:
            self.minval.append(val)
        else:
            if val < self.minval[-1]:
                self.minval.append(val)
            else:
                self.minval.append(self.minval[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]
