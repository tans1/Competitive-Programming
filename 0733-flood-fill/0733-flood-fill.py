class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or (i,j) in visited or image[i][j] != initial:
                return
            
            visited.add((i,j))
            image[i][j] = color
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        visited = set()
        initial = image[sr][sc]
        dfs(sr, sc)
        return image
            
            