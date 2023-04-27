class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        
        visited = set()
        row, col = len(grid), len(grid[0])
        q = deque()
        directions = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        if grid[0][0] == 0:
            q.append([(0,0,1)])
            visited.add((0,0))
            
        while q:
            cur_level = q.popleft()
            next_level = []
            
            for r,c,t in cur_level:
                if r == row-1 and c == col - 1:
                    return t
                for i , j in directions:
                    if 0 <= r+i < row and 0 <= c+j < col and (r+i,c+j) not in visited and grid[r+i][c+j] == 0:
                        next_level.append((r+i,c+j,t+1))
                        visited.add((r+i,c+j))
            
            if next_level:
                q.append(next_level)
        
        return -1
                