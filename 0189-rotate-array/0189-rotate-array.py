class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            a = nums.pop()
            nums.insert(0,a)
            i +=1
    
    
        
            