import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        temp2 = list(heapq.merge(temp[:m],nums2))
        for i in range(len(temp2)):
            nums1[i] = temp2[i]
        print(nums1)
        
