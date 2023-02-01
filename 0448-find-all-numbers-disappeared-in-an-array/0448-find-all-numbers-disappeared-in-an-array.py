class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [i for i in range(1,n+1)]
        set1 = set(temp)
        set2 = set(nums)
        
        temp2 = set1 - set2
        
        res = []
        for n in temp2:
            res.append(n)
        res.sort()
        return res