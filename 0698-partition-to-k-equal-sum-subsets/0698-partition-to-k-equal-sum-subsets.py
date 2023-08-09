class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0 or len(nums) < k:
            return False
        
        nums.sort(reverse = True)

        used = [False] * len(nums)
        target = sum(nums) / k
        
        @lru_cache
        def backtrack(i,K,subsetSum):
            if K == 0:
                return True
            if subsetSum == target:
                return backtrack(0,K-1,0)
            
            for j in range(i,len(nums)):
                if used[j] == True:
                    continue
                    
                used[j] = True

                if backtrack(j+1, K , subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0,k,0)