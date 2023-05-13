class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = list(map(lambda x: -x, piles))
        heapq.heapify(heap)
        
        while k:
            nm = heapq.heappop(heap)
            heapq.heappush(heap,nm//2)
            k -= 1
        
        return sum(heap) * -1