class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        
        self.stack = []
        self.size = 0

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.stack.append(num)
            self.size += 1
        else:
            self.stack = []
            self.size = 0
        
        return self.size >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)