class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        temp =[0 for _ in range(n+1)]
        
        for rq in requests:
            temp[rq[0]] += 1
            temp[rq[1] + 1] -= 1

        for i in range(1,n+1):
            temp[i] += temp[i-1]
            
        temp.sort()
        temp.reverse()
        nums.sort()
        nums.reverse()
        res = 0

        for i in range(n):
            res += (temp[i] * nums[i])
        return res % (10**9 + 7)
        
