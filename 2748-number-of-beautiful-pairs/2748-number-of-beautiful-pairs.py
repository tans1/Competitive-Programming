class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def coprimes(n,m):
            for i in range(2,10):
                if n % i == 0 and m % i == 0:
                    return False
            
            return True
        
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                ans += coprimes(int(str(nums[i])[0]), int(str(nums[j])[-1]))
        
        return ans
    