class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        def likeTimeCoefficient(arr):
            result = 0
            for i, v in enumerate(arr):
                result += v*(i+1)
            return result
        
        satisfaction.sort()
        dct = {}
        for i in range(len(satisfaction)-1,-1,-1):
            dct[i] = likeTimeCoefficient(satisfaction[i:])
        
        ans = max(dct.values())
        if ans >= 0:
            return ans
        return 0