class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = [0]
        
        for i in range(len(nums)):
            if pre[-1] + nums[i] >= nums[i]:
                pre.append(pre[-1] + nums[i])
            else:
                pre.append(nums[i])
        return max(pre[1:])
                