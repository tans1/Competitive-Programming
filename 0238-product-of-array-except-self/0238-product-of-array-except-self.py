class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        
        for i in range(1,len(nums)):
            pre.append(pre[-1] * nums[i-1])
        for j in range(len(nums)-2,-1,-1):
            post.append(post[-1] * nums[j+1])
        post.reverse()
        
        ans = []
        
        for i in range(len(pre)):
            ans.append(pre[i] * post[i])
        return ans

        
    
