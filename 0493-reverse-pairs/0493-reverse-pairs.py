class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums):
            if len(nums) <= 1:
                return 0
            md = (len(nums)) // 2
            left = nums[:md]
            right = nums[md:]
            
            res = merge_sort(left) + merge_sort(right)
            
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j] * 2:
                    res += len(right) - j
                    i += 1
                else:
                    j += 1
            
            l = 0
            r = 0
            k = 0
            while l < len(left) and r < len(right):
                if left[l] >= right[r]:
                    nums[k] = left[l]
                    l += 1
                else:
                    nums[k] = right[r]
                    r += 1
                
                k += 1
            
            while l < len(left):
                nums[k] = left[l]
                l += 1
                k += 1
            while r < len(right):
                nums[k] = right[r]
                r += 1
                k += 1
            return res
        
        return merge_sort(nums)
        