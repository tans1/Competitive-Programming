class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]
        
        mx = height[0]
        for i in range(1,len(height)):
            maxLeft[i] = mx
            mx = max(mx, height[i])
        n = len(height)
        mx = height[n-1]
        for i in range(n-2,-1,-1):
            maxRight[i] = mx
            mx = max(mx,height[i])
        
        ans = 0
        for i,v in enumerate(height):
            ans += max(0, min(maxLeft[i], maxRight[i])-v)
        return ans
                    
        