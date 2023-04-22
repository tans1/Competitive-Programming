class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j, cur):
            if i<0 or j<0 or i >= len(grid1) or j >= len(grid1[0]) or (i,j) in visited or grid2[i][j] == 0:
                return
            
            visited.add((i,j))
            cur.add((i,j))
            for l,k in direction:
                dfs(l+i,k+j, cur)
            return cur
        ans = 0
        visited = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if (i,j) not in visited and grid2[i][j] == 1:
                    temp = dfs(i,j,set())
                    if temp:
                        flag = True
                        for m,n in temp:
                            if grid1[m][n] == 0:
                                flag = False
                        if flag:
                            ans += 1
        return ans
    
