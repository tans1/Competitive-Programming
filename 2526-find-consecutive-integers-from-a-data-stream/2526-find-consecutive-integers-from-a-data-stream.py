class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        
        self.stack = []

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.stack.append(num)
        else:
            self.stack = []
        
        return len(self.stack) >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)