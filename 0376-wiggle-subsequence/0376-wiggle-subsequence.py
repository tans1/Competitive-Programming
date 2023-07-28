class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc_ = 1
        dec_ = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_ = dec_ + 1
                
            elif nums[i] < nums[i - 1]:
                dec_ = inc_ + 1

        return max(dec_, inc_)