class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            val = x - self.min
            self.stack.append(val)
            if val < 0:
                self.min = x

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val


    def top(self) -> int:
        top = self.stack[-1]
        if top >= 0:
            return self.min + top
        return self.min

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
