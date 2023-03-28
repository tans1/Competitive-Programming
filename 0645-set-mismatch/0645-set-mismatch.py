class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = [0 for i in range(len(nums)+1)]
        for n in nums:
            temp[n] += 1
        
        ans = []
        for i in range(len(temp)):
            if temp[i] > 1:
                ans.append(i)
        for i in range(1, len(temp)):
            if temp[i] == 0:
                ans.append(i)
        
        return ans
        
            