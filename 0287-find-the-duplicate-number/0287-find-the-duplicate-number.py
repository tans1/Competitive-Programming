class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            temp = 1 << n
            
            if res == (temp | res):
                return n
            else:
                res = res | temp
        
        