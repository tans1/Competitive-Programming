class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i,prev_robbed):
            nonlocal ans
            if i + 1 == len(nums):
                if prev_robbed: 
                    return 0
                else:
                    return nums[i]
            
            if (i,prev_robbed) in memo:
                return memo[(i,prev_robbed)]
            
            if prev_robbed:
                temp = dfs(i+1,not prev_robbed)
            else:
                temp = max(dfs(i+1,not prev_robbed) + nums[i], dfs(i+1, prev_robbed))
            memo[(i,prev_robbed)] = temp
            return temp
        
        ans = dfs(0,False)
        return ans
                
                
                
            