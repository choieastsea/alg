class MinStack:

    def __init__(self):
        self.stack = [] # [[val, min_val]...]로 구성

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.stack[-1][1] if len(self.stack)>0 else 2**32, val)))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()