class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = list(map(lambda x: -x, nums))
        cnt = 0
        heapq.heapify(nums)
        total1 = sum(nums)
        total2 = sum(nums)
        
        while 2*total2 < total1:
            mx = heapq.heappop(nums)
            total2 -= (mx / 2)
            cnt += 1
            heapq.heappush(nums, mx / 2)
        return cnt