class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Rcounter=Wcounter=Bcounter = 0
        for i in nums:
            if i == 0:
                Rcounter +=1
        for i in nums:
            if i == 1:
                Wcounter +=1
        for i in nums:
            if i == 2:
                Bcounter +=1
        if Rcounter != 0:
            j = 0
            i = 0 
            while i < Rcounter:
                nums[j] = 0
                j +=1
                i +=1
        if Wcounter != 0:
            j = Rcounter
            i = 0
            while i < Wcounter:
                nums[j] = 1
                j +=1
                i +=1
        if Bcounter != 0:
            j = Wcounter + Rcounter
            i = 0
            while i < Bcounter:
                nums[j] = 2
                j +=1
                i +=1

            