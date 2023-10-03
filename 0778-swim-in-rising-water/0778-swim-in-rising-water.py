class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ans = float('-inf')
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def in_bound(row,col):
            return 0  <= row < len(grid) and 0  <= col < len(grid[0]) 
        
        priority_queue = [(grid[0][0],(0,0))]
        
        heapq.heapify(priority_queue)
        
        visited = set()
        
        while priority_queue:
            
            val,idx = heapq.heappop(priority_queue)
            
            if idx in visited:
                continue
                
            ans = max(val,ans)
            if idx == (len(grid)-1,len(grid[0])-1):
                return ans
            
            visited.add(idx)
            
            for direction in directions:
                
                new_row = direction[0] + idx[0]
                new_col = direction[1] + idx[1]
                
                if in_bound(new_row,new_col):
                    
                    heapq.heappush(priority_queue,(grid[new_row][new_col],(new_row,new_col)))