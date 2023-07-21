class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        ans = [[float('inf') for _ in range(col)] for _ in range(row)]
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        q = deque()
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    visited.add((i,j))
                    ans[i][j] = 0
        
        while q:
            i,j, cst = q.popleft()
            
            for r,c in directions:
                if 0 <= i+r < row and 0 <= j+c < col and (i+r,j+c) not in visited:
                    if mat[i+r][j+c] == 0:
                        ans[i+r][j+c] = 0
                        q.append((i+r,j+c,0))
                    else:
                        ans[i+r][j+c] = min(ans[i+r][j+c], cst+1)
                        q.append((i+r,j+c,cst+1))
                    visited.add((i+r,j+c))
                
        return ans