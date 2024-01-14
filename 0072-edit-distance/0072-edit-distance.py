class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        grid = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word1[j] == word2[i]:
                    if not(0 <= i -1 < len(word2)) and not(0 <= j -1 < len(word1)):
                        grid[i][j] = 0
                    elif 0 <= i -1 < len(word2) and not(0 <= j -1 < len(word1)):
                        grid[i][j] = i
                    elif  not(0 <= i -1 < len(word2)) and 0 <= j -1 < len(word1):
                        grid[i][j] = j
                    elif 0 <= i -1 < len(word2) and 0 <= j -1 < len(word1):
                        grid[i][j] = grid[i-1][j-1] 
                else:
                    top = float('inf')
                    left = float('inf')
                    cross = float('inf')
                    
                    if 0 <= i -1 < len(word2):
                        top = grid[i-1][j]
                    if 0 <= j -1 < len(word1):
                        left = grid[i][j-1]
                    if 0 <= i -1 < len(word2) and 0 <= j -1 < len(word1):
                        cross =  grid[i-1][j-1]
                    if min(left,top,cross) < float('inf'):
                        grid[i][j] = 1 + min(left, top,cross)
                    
                    else:
                        grid[i][j] = 1
        print(grid)        
        return grid[-1][-1]
          
            