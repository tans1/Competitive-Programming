class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        skip = [0 for _ in range(100001)]
        take = [0 for _ in range(100001)]
        values = [0 for _ in range(100001)]
        
        for n in nums:
            values[n] += n
        
        for i in range(100001):
            take[i] = skip[i-1] + values[i]
            skip[i] = max(take[i-1], skip[i-1])
        
        return max(max(take),max(skip))
        