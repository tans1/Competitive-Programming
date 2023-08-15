class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-v for i,v in enumerate(stones)]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            y , x = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            
            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, -1 * ((-1 * y) - (-1 * x)))
                
        if len(maxHeap) == 1:
            return maxHeap[0]*-1
        return 0