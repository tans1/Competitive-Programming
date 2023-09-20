class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        cur_sum = 0
        i = 0
        ans = n + 1
        
        for j in range(n):
            cur_sum += nums[j]
            while cur_sum > target and i <= j:
                cur_sum -= nums[i]
                i += 1
            
            if cur_sum == target:
                ans = min(ans, n- (j-i+1))
                
        if ans == n+1:
            return -1
        return ans
                
                