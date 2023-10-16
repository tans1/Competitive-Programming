class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        
        self.stack1.append(val)
        self.stack2.append(val)
        
        if self.stack2:
            self.stack2.sort()
            
    def pop(self) -> None:
        
        if (self.stack2):
            indx = self.stack2.index(self.stack1[-1])
            del self.stack2[indx]
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()