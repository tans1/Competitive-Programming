class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        
        self.queue = deque()
        self.odd = 0
    def consec(self, num: int) -> bool:
        if self.value != num:
            self.odd += 1
        self.queue.append(num)
        
        if len(self.queue) < self.k :
            return False
    
        elif len(self.queue) == self.k:
            return self.odd == 0
        
        else:
            if self.queue[0] != self.value:
                self.odd -= 1
            self.queue.popleft()
            return self.odd == 0
            
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)