class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        suffix_sum = [0 for _ in range(len(satisfaction))]
        for i in range(len(satisfaction)-2,-1,-1):
            suffix_sum[i] = suffix_sum[i+1] + satisfaction[i+1]
        
        temp = [0 for _ in range(len(satisfaction) + 1)]
        for i in range(len(satisfaction)-1,-1,-1):
            temp[i] = temp[i+1] + satisfaction[i] + suffix_sum[i]
        ans = max(temp[:len(satisfaction)])

        if ans > 0:
            return ans
        return 0
        