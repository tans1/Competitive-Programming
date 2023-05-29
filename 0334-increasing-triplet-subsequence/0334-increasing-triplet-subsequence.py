class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftmin , rightmin , mono = [] , [] , []
        mono = []
        for n in nums:
            if mono:
                leftmin.append(mono[-1])
            else:
                leftmin.append('-')
            
            while mono and mono[-1] >= n:
                mono.pop()
            if not mono or (mono and mono[-1] > n):
                mono.append(n)
        
        mono2 = []
        for i in range(len(nums)-1,-1,-1):
            if mono2:
                rightmin.append(mono2[-1])
            else:
                rightmin.append('-')
            
            while mono2 and mono2[-1] <= nums[i]:
                mono2.pop()
            if not mono2 or (mono2 and mono2[-1] <= nums[i]):
                mono2.append(nums[i])
        
        rightmin.reverse()
        for i in range(len(nums)):
            if leftmin[i] != '-' and rightmin[i] != '-':
                if leftmin[i] < nums[i] < rightmin[i]:
                    return True
        return False
            

                        
                
                