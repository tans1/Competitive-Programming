class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        n = len(arr)
        
        while left < n and right > -1 and  left <= right:
            md = (left + right ) // 2

            if arr[md-1] < arr[md] and arr[md] > arr[md + 1]:
                return md
            elif (arr[md-1] < arr[md]) and not (arr[md] > arr[md+1]):
                left = md 
            elif not (arr[md-1] < arr[md]) and (arr[md] > arr[md + 1]):
                right = md 