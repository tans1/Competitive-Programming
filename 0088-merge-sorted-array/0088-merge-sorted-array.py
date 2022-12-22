class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1: return nums2
        if not nums2: return nums1
        
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()
        return
    ########################################
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k], nums1[i] = nums1[i], nums1[k]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        print(nums1)
