class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater2 = [-1 for _ in range(len(nums2))]
        
        for i in range(len(nums2)):
            j = i
            while j < len(nums2) and nums2[i] >= nums2[j]:
                j += 1

            if j < len(nums2) and nums2[i] < nums2[j]:
                nextGreater2[i] = nums2[j]
        
        ans= [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2) and nums1[i] != nums2[j]:
                j += 1
            ans[i] = nextGreater2[j]
        return ans