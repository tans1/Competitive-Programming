class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_prefix = grid[0].copy()
        bottom_prefix = grid[1].copy()
        
        for i in range(1, n):
            top_prefix[i] += top_prefix[i-1]
            bottom_prefix[i] += bottom_prefix[i-1]
        
        res = float('inf')
        for i in range(n):
            top_right = top_prefix[-1] - top_prefix[i]
            bottom_left = bottom_prefix[i-1] if i > 0 else 0
            
            second_player = max(top_right, bottom_left)
            res = min(res, second_player)
        return res