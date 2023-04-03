class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge_sort(nums):
            if len(nums) <= 1: return 0
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            res = merge_sort(left) + merge_sort(right)

            
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    res += (len(right) - j)
                    i += 1
                else:
                    j += 1
            
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    nums[k] = right[j]
                    j += 1
                else:
                    nums[k] = left[i]
                    i += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            
            return res

        df = [(nums1[i] - nums2[i]) for i in range(len(nums1))]
        return merge_sort(df) 