class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        n = len(temp)
        
        if n == 0:
            return 0
        elif n % 2 != 0:
            return temp[n//2]
        else:
            return (temp[n//2 - 1] + temp[n//2] ) / 2