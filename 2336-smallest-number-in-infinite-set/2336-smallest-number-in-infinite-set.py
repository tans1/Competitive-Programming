class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1,1001)]
        self.present = [True for _ in range(1001)]
        heapq.heapify(self.heap)
    def popSmallest(self) -> int:
        ans = heapq.heappop(self.heap)
        self.present[ans] = False
        return ans

    def addBack(self, num: int) -> None:
        if self.present[num] == False:
            heapq.heappush(self.heap, num)
            self.present[num] = True
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)