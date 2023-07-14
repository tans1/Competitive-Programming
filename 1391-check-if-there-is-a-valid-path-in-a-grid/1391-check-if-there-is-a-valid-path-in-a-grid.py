class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        paths = {
            1 : {'left' : [1,4,6],'right'  : [1,3,5]},
            2 : {'top'  : [2,3,4],'bottom' : [2,5,6]},
            3 : {'left' : [1,4,6],'bottom' : [2,5,6]},
            4 : {'right': [1,3,5],'bottom' : [2,5,6]},
            5 : {'top'  : [2,3,4],'left'   : [1,4,6]},
            6 : {'top'  : [2,3,4],'right'  : [1,3,5]}
        }
        direc = [(0,-1),(0,1),(1,0),(-1,0)]
        visited = set()
        ans = False
        def dfs(i,j):
            nonlocal ans
            if i == m-1 and j == n-1:
                ans = True
                return True
            
            for l,k in direc:
                if 0 <= i+l < m and 0 <= j+k < n and (i+l,j+k) not in visited:
                    if grid[i][j] == 1:
                        if (l,k) == (0,-1) and grid[i+l][j+k] in paths[grid[i][j]]['left'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (0,1) and grid[i+l][j+k] in paths[grid[i][j]]['right']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                    elif grid[i][j] == 2:
                        if (l,k) == (-1,0) and grid[i+l][j+k] in paths[grid[i][j]]['top'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (1,0) and grid[i+l][j+k] in paths[grid[i][j]]['bottom']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                    elif grid[i][j] == 3:
                        if (l,k) == (0,-1) and grid[i+l][j+k] in paths[grid[i][j]]['left'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (1,0) and grid[i+l][j+k] in paths[grid[i][j]]['bottom']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                    elif grid[i][j] == 4:
                        if (l,k) == (0,1) and grid[i+l][j+k] in paths[grid[i][j]]['right'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (1,0) and grid[i+l][j+k] in paths[grid[i][j]]['bottom']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                    elif grid[i][j] == 5:
                        if (l,k) == (0,-1) and grid[i+l][j+k] in paths[grid[i][j]]['left'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (-1,0) and grid[i+l][j+k] in paths[grid[i][j]]['top']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                    elif grid[i][j] == 6:
                        if (l,k) == (-1,0) and grid[i+l][j+k] in paths[grid[i][j]]['top'] :
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)
                        elif (l,k) == (0,1) and grid[i+l][j+k] in paths[grid[i][j]]['right']:
                            visited.add((i+l,j+k))
                            dfs(i+l,j+k)

            return False
        visited.add((0,0))
        dfs(0,0)
        return ans
            
            