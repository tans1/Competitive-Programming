class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return

            visited.add((i,j))
            for l ,k in directions:
                if (i+l,j+k) not in visited:
                    dfs(i +l, j + k)

            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res