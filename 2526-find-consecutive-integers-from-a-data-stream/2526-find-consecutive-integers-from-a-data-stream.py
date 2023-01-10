class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.temp = 0

    def consec(self, num: int) -> bool:
        
        if num == self.value:
            self.temp += 1
        else:
            self.temp = 0
        return self.temp >= self.k
    


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)