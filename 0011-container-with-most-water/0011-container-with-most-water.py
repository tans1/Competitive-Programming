class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            heightt = min(height[left], height[right])
            area = heightt * (right-left)
            maxx = max(maxx,area)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxx