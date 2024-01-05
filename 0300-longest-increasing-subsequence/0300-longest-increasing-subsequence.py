class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seqLength = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
          for j in range(i,-1,-1):
            if nums[j] < nums[i]:
              seqLength[i] = max(seqLength[i], seqLength[j] + 1)
        return max(seqLength)