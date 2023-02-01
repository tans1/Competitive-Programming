class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        base = [i for i in range(1,len(nums)+1)]
        set1 = set(base)
        set2 = set(nums)
        
        difference = set1 - set2
        
        res = []
        for n in difference:
            res.append(n)
        res.sort()
        return res