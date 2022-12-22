class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for k,v in freq.items():
            comb = (v * (v-1)) // 2
            res += comb
        return res
        counter = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    counter +=1
        return counter