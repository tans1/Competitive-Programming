class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        def island_finder(i,j,island):
            if (i,j) in visited or grid[i][j] == 0:
                return
            island.append((i,j,0))
            visited.add((i,j))
            for l,k in direction:
                if 0 <= i+l < len(grid) and 0 <= j+k < len(grid[0]) :
                    island_finder(i+l,j+k,island)
            return island
        
        def bfs(q):
            while q:
                i,j,dst = q.popleft()
                for l,k in direction:
                    if 0 <= i+l < len(grid) and 0 <= j+k < len(grid[0]) and (i+l,j+k) not in visited:
                        if grid[i+l][j+k] == 1:
                            return dst
                        q.append((i+l,j+k,dst+1))
                        visited.add((i+l,j+k))
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = island_finder(i,j,[])
                    q = deque(island)
                    return bfs(q)
        
        