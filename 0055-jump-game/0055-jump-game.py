class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif len(nums) == 2:
            return nums[0] > 0
        else:
            n = len(nums)
            i = n-1
            j = i - 1

            while i > 0 :
                while nums[j] < i - j and j > 0:
                    j -= 1

                if nums[j] < i - j:
                    return False

                i = j
                j -= 1
            return True
        
        
        # starting from the end check that , "can we reach the current nums[i] from nums[j] ?"